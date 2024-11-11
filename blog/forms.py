from django import forms
from .models import Post, Comment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class PostForm(forms.ModelForm):
    """
    A form for creating and updating Post instances.
    
    Meta:
    - model: The model associated with this form (Post).
    - fields: The fields of the Post model to be included in the form.
    - widgets: Custom widgets for the fields.
    """
    class Meta:
        model = Post
        fields = ['title', 'content', 'image', 'category']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        }
        
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['title'].required = True
        self.fields['content'].required = True
        self.fields['image'].required = True
        self.fields['category'].required = True


class CustomUserCreationForm(UserCreationForm):
    """
    A form for creating new users, with email field required.
    
    Fields:
    - email: An email field required for user registration.
    """
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        """
        Save the provided password in hashed format and email.
        
        Parameters:
        - commit: Boolean indicating whether to save the model instance.
        
        Returns:
        - user: The saved user instance.
        """
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class CommentForm(forms.ModelForm):
    """
    A form for creating and updating Comment instances.
    
    Meta:
    - model: The model associated with this form (Comment).
    - fields: The fields of the Comment model to be included in the form.
    - widgets: Custom widgets for the fields.
    """
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        }
        
class ProfileUpdateForm(forms.ModelForm):
    """
    A form for updating user profile information.
    
    Meta:
    - model: The model associated with this form (User).
    - fields: The fields of the User model to be included in the form.
    """
    class Meta:
        model = User
        fields = ['username', 'email']
