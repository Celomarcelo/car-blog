from django.contrib import admin
from .models import Post, Category, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """
    Admin interface options for the Post model.
    """
    list_display = ('title', 'author', 'created_at', 'approved')
    list_filter = ('approved', 'created_at')
    search_fields = ('title', 'content')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Admin interface options for the Category model.
    """
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Admin interface options for the Comment model.
    """
    list_display = ('author', 'content', 'created_at', 'approved')
    list_filter = ('approved', 'created_at')
    search_fields = ('author__username', 'content')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        """
        Custom admin action to approve selected comments.
        """
        queryset.update(approved=True)
        self.message_user(request, "Selected comments were approved.")
    approve_comments.short_description = 'Approve selected comments'
