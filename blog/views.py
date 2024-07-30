from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Post, Category
from .forms import PostForm, CustomUserCreationForm, CommentForm
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy

# View function for the home page
def home(request):
    posts = Post.objects.filter(approved=True).order_by('-created_at')
    categories = Category.objects.all()
    return render(request, 'home.html', {'posts': posts, 'categories': categories})

# View function to filter posts by category
def category_filter(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    posts = Post.objects.filter(category=category, approved=True)
    categories = Category.objects.all()
    return render(request, 'category.html', {'posts': posts, 'categories': categories, 'selected_category': category})

# View function to create a new post, accessible only to logged-in users
@login_required
def new_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('home')
    else:
        form = PostForm()

    return render(request, 'new_post.html', {'form': form})

# View function to display all posts by a specific user
@login_required
def user_posts(request, username):
    user = get_object_or_404(User, username=username)
    posts = Post.objects.filter(author=user)
    return render(request, 'user_posts.html', {'user': user, 'posts': posts})

# View function to display the details of a specific post
@login_required
def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = post.comments.filter(approved=True)

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.author = request.user
            new_comment.save()
            return redirect('post_detail', post_id=post.id)
    else:
        comment_form = CommentForm()

    return render(request, 'post_detail.html', {
        'post': post,
        'comments': comments,
        'comment_form': comment_form,
    })

# View function to edit a specific post, accessible only to logged-in users
@login_required
def post_edit(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', post_id=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'post_edit.html', {'form': form, 'post': post})

# View function to delete a specific post, accessible only to logged-in users
@login_required
def post_delete(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        post.delete()
        return redirect('user_posts', username=post.author.username)
    return render(request, 'post_confirm_delete.html', {'post': post})


# View function to handle user registration
def register(request):
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

# View to display the user's profile
@login_required
def profile(request):
    user = request.user
    return render(request, 'profile.html', {'user': user})

class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'password_reset_confirm.html'
    success_url = reverse_lazy('profile')
    form_class = PasswordChangeForm

# View to edit the user's profile
@login_required
def edit_profile(request):
    user = request.user
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserChangeForm(instance=user)

    return render(request, 'edit_profile.html', {'form': form})
