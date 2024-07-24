from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Post, Category
from .forms import PostForm, CustomUserCreationForm
from django.contrib.auth.models import User
import logging
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.conf import settings


def home(request):
    posts = Post.objects.filter(approved=True)
    categories = Category.objects.all()
    return render(request, 'home.html', {'posts': posts, 'categories': categories})

def category_filter(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    posts = Post.objects.filter(category=category, approved=True)
    categories = Category.objects.all()
    return render(request, 'category.html', {'posts': posts, 'categories': categories, 'selected_category': category})


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

@login_required
def user_posts(request, username):
    user = get_object_or_404(User, username=username)
    posts = Post.objects.filter(author=user)
    return render(request, 'user_posts.html', {'user': user, 'posts': posts})

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'post_detail.html', {'post': post})

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


def post_delete(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        post.delete()
        return redirect('user_posts', username=post.author.username)
    return render(request, 'post_confirm_delete.html', {'post': post})



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

logger = logging.getLogger(__name__)

def password_reset_view(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            try:
                associated_users = User.objects.filter(email=data)
                if associated_users.exists():
                    for user in associated_users:
                        subject = "Password Reset Requested"
                        email_template_name = "password_reset_email.html"
                        c = {
                            "email": user.email,
                            'domain': request.META['HTTP_HOST'],
                            'site_name': 'Your Site',
                            "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                            "user": user,
                            'token': default_token_generator.make_token(user),
                            'protocol': 'http',
                        }
                        email = render_to_string(email_template_name, c)
                        send_mail(subject, email, settings.DEFAULT_FROM_EMAIL, [user.email], fail_silently=False)
                return render(request, 'password_reset_done.html')
            except Exception as e:
                logger.error(f"Erro na redefinição de senha: {e}")
                return render(request, 'error_template.html', {'error_message': str(e)})
    else:
        password_reset_form = PasswordResetForm()
    return render(request, 'password_reset.html', {'password_reset_form': password_reset_form})