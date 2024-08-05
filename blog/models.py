from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    """
    Model representing a category for posts.
    
    Fields:
    - name: The name of the category.
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        """
        String representation of the Category model.
        
        Returns:
        - str: The name of the category.
        """
        return self.name


class Post(models.Model):
    """
    Model representing a blog post.
    
    Fields:
    - title: The title of the post.
    - content: The content of the post.
    - author: The author of the post, linked to the User model.
    - created_at: The date and time the post was created.
    - updated_at: The date and time the post was last updated.
    - approved: A boolean indicating whether the post has been approved.
    - category: The category the post belongs to, linked to the Category model.
    - image: An optional image associated with the post.
    """
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='posts', null=True, blank=True)
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)

    def __str__(self):
        """
        String representation of the Post model.
        
        Returns:
        - str: The title of the post.
        """
        return self.title


class Comment(models.Model):
    """
    Model representing a comment on a post.
    
    Fields:
    - post: The post the comment is associated with, linked to the Post model.
    - author: The author of the comment, linked to the User model.
    - content: The content of the comment.
    - created_at: The date and time the comment was created.
    - approved: A boolean indicating whether the comment has been approved.
    """
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        """
        String representation of the Comment model.
        
        Returns:
        - str: A string indicating the author and the post the comment is associated with.
        """
        return f'Comment by {self.author} on {self.post}'
