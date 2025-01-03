from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


"""
URL configuration for the blog application.
Includes routes for home, post details, user posts, and more.
"""
urlpatterns = [
    # Home page of the blog
    path('', views.home, name='home'),
    
    # Page to create a new blog post
    path('new/', views.new_post, name='new_post'),
    
    # Page to register a new user
    path('register/', views.register, name='register'),
    
    # Login page for users
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    
    # Logout page for users
    path('logout/', views.custom_logout, name='logout'),
    path('logged_out/', auth_views.LogoutView.as_view(template_name='logged_out.html'), name='logout'),
    
    # Page to display all posts by a specific user
    path('user/<str:username>/posts/', views.user_posts, name='user_posts'),
    
    # Page to display details of a specific post
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),
    
    # Page to delete user comment
    path('comment/<int:comment_id>/delete/', views.comment_delete, name='comment_delete'),
    
    # Page to edit a specific post
    path('post/<slug:slug>/edit/', views.post_edit, name='post_edit'),
    
    # Page to delete a specific post
    path('post/<slug:slug>/delete/', views.post_delete, name='post_delete'),
    
    # Page to filter posts by a specific category
    path('category/<int:category_id>/',
         views.category_filter, name='category_filter'),
    
    # Page to reset the user's password
    path('password_reset/', auth_views.PasswordResetView.as_view(),
         name='password_reset'),
    
    # Page shown after the password reset request has been done
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(),
         name='password_reset_done'),
    
    # Page to confirm the password reset using a unique token
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    
    # Page shown after the password has been successfully reset
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),
    
    # URL pattern for displaying the user's profile 
    path('profile/', views.profile, name='profile'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
