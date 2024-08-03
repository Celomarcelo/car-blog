from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    """
    Model representing a category for posts.
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        """
        String representation of the Category model.
        """
        return self.name


class Post(models.Model):
    """
    Model representing a blog post.
    """
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='posts', null=True, blank=True)
    image = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        """
        String representation of the Post model.
        """
        return self.title


class Comment(models.Model):
    """
    Model representing a comment on a post.
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
        """
        return f'Comment by {self.author} on {self.post}'
