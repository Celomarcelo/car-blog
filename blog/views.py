from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import authenticate, login, update_session_auth_hash, logout
from django.contrib.auth.decorators import login_required
from .models import Post, Category, Comment
from .forms import PostForm, CustomUserCreationForm, CommentForm, ProfileUpdateForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.decorators.http import require_POST
from django.core.exceptions import PermissionDenied


def home(request):
    """
    View function for the home page.

    Displays all approved posts ordered by creation date and all categories.

    Parameters:
    - request: The HTTP request object.

    Returns:
    - HTTPResponse: Renders the home page with posts and categories.
    """
    posts = Post.objects.filter(approved=True).order_by('-created_at')
    categories = Category.objects.all()
    return render(request, 'home.html', {'posts': posts, 'categories': categories})


def category_filter(request, category_id):
    """
    View function to filter posts by category.

    Parameters:
    - request: The HTTP request object.
    - category_id: The ID of the category to filter posts by.

    Returns:
    - HTTPResponse: Renders the category page with filtered posts.
    """
    category = get_object_or_404(Category, id=category_id)
    posts = Post.objects.filter(category=category, approved=True)
    categories = Category.objects.all()
    return render(request, 'category.html', {'posts': posts, 'categories': categories, 'selected_category': category})


@login_required
def new_post(request):
    """
    View function to create a new post, accessible only to logged-in users.

    Parameters:
    - request: The HTTP request object.

    Returns:
    - HTTPResponse: Redirects to home page after creating a post or renders the new post form.
    """
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.warning(
                request, 'Your post is under analysis by the administrator.')
            return redirect('home')
        else:
            messages.error(
                request, 'There was an error with your post. Please try again.')
    else:
        form = PostForm()

    return render(request, 'new_post.html', {'form': form})


@login_required
def user_posts(request, username):
    """
    View function to display all posts by a specific user.

    Parameters:
    - request: The HTTP request object.
    - username: The username of the user whose posts are to be displayed.

    Returns:
    - HTTPResponse: Renders the user posts page with the user's posts.
    """
    user = get_object_or_404(User, username=username)
    posts = Post.objects.filter(author=user)
    return render(request, 'user_posts.html', {'user': user, 'posts': posts})


@login_required
def post_detail(request, post_id):
    """
    View function to display the details of a specific post.

    Parameters:
    - request: The HTTP request object.
    - post_id: The ID of the post to display.

    Returns:
    - HTTPResponse: Renders the post detail page with comments and comment form.
    """
    post = get_object_or_404(Post, id=post_id)
    comments = post.comments.filter(approved=True)

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.author = request.user
            new_comment.save()
            messages.warning(
                request, 'Your comment is under analysis by the administrator.')
            return redirect('post_detail', post_id=post.id)
        else:
            messages.error(
                request, 'There was an error with your comment. Please try again.')
    else:
        comment_form = CommentForm()

    return render(request, 'post_detail.html', {
        'post': post,
        'comments': comments,
        'comment_form': comment_form,
    })


@login_required
def comment_delete(request, comment_id):
    """
    View function to delete a specific comment, accessible only to the comment author.
    """
    comment = get_object_or_404(Comment, id=comment_id)

    # Ensure that the user trying to delete the comment is the author
    if comment.author != request.user:
        messages.error(
            request, "You don't have permission to delete this comment.")
        return redirect('post_detail', post_id=comment.post.id)

    if request.method == 'POST':
        try:
            comment.delete()
            messages.success(request, 'Comment deleted successfully.')
            return redirect('post_detail', post_id=comment.post.id)
        except Exception as e:
            messages.error(
                request, 'An error occurred while trying to delete the comment. Please try again.')

    return render(request, 'comment_confirm_delete.html', {'comment': comment})


@login_required
def post_edit(request, post_id):
    """
    View function to edit a specific post, accessible only to logged-in users.
    Allows editing only if the logged-in user is the author of the post.

    Parameters:
    - request: The HTTP request object.
    - post_id: The ID of the post to be edited.

    Returns:
    - HTTPResponse: Redirects to post detail page after editing or renders the edit post form.
    """

    post = get_object_or_404(Post, pk=post_id)

    if post.author != request.user:
        messages.error(request, "You don't have permission to edit this post.")
        return redirect('post_detail', post_id=post_id)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)

        if form.is_valid():
            form.save()
            messages.success(request, 'Post saved!')
            return redirect('post_detail', post_id=post_id)
        else:
            messages.error(
                request, 'An error occurred while trying to edit the post. Please try again.')
    else:
        form = PostForm(instance=post)

    return render(request, 'post_edit.html', {'form': form, 'post': post})


@login_required
def post_delete(request, post_id):
    """
    View function to delete a specific post, accessible only to logged-in users.

    Parameters:
    - request: The HTTP request object.
    - post_id: The ID of the post to be deleted.

    Returns:
    - HTTPResponse: Redirects to the user's posts page after deletion or renders the delete confirmation page.
    """
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        try:
            post.delete()
            messages.success(
                request, f'The post "{post.title}" was successfully deleted.')
            return redirect('user_posts', username=post.author.username)
        except Exception as e:
            messages.error(
                request, 'An error occurred while trying to delete the post. Please try again.')
        return redirect('post_detail', post_id=post_id)
    return render(request, 'post_confirm_delete.html', {'post': post})


def register(request):
    """
    View function to handle user registration.

    Parameters:
    - request: The HTTP request object.

    Returns:
    - HTTPResponse: Redirects to home page after successful registration or renders the registration form.
    """
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})


@login_required
def profile(request):
    """
    View to display the user's profile.

    Handles profile updates and password changes.

    Parameters:
    - request: The HTTP request object.

    Returns:
    - HTTPResponse: Redirects to profile page after updating profile or changing password, or renders the profile form.
    """
    profile_form = ProfileUpdateForm(instance=request.user)
    password_form = PasswordChangeForm(request.user)

    if request.method == 'POST':
        if 'update_profile' in request.POST:
            profile_form = ProfileUpdateForm(
                request.POST, instance=request.user)
            if profile_form.is_valid():
                profile_form.save()
                messages.success(
                    request, 'Your profile has been successfully updated.')
                return redirect('profile')
        elif 'change_password' in request.POST:
            password_form = PasswordChangeForm(request.user, request.POST)
            if password_form.is_valid():
                user = password_form.save()
                update_session_auth_hash(request, user)
                messages.success(
                    request, 'Your password has been successfully changed.')
                return redirect('profile')

    context = {
        'profile_form': profile_form,
        'password_form': password_form,
    }

    return render(request, 'profile.html', context)


@require_POST
def custom_logout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('logged_out')
    return redirect('/')
