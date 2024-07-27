from django.test import TestCase
from .models import Category, Post, Comment
from django.contrib.auth.models import User


class CategoryModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Technology")

    def test_category_str(self):
        self.assertEqual(str(self.category), "Technology")
        
class PostModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.category = Category.objects.create(name='Django')
        self.post = Post.objects.create(
            title='Django Testing',
            content='Content of the post',
            author=self.user,
            category=self.category
        )

    def test_post_creation(self):
        self.assertEqual(self.post.title, 'Django Testing')
        self.assertEqual(self.post.content, 'Content of the post')
        self.assertEqual(self.post.author.username, 'testuser')
        self.assertEqual(self.post.category.name, 'Django')
        self.assertFalse(self.post.approved)
        self.assertEqual(str(self.post), 'Django Testing')

class CommentModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.category = Category.objects.create(name='Django')
        self.post = Post.objects.create(
            title='Django Testing',
            content='Content of the post',
            author=self.user,
            category=self.category
        )
        self.comment = Comment.objects.create(
            post=self.post,
            author=self.user,
            content='This is a comment'
        )

    def test_comment_creation(self):
        self.assertEqual(self.comment.post.title, 'Django Testing')
        self.assertEqual(self.comment.author.username, 'testuser')
        self.assertEqual(self.comment.content, 'This is a comment')
        self.assertFalse(self.comment.approved)
        self.assertEqual(str(self.comment), f'Comment by {self.comment.author} on {self.comment.post}')

