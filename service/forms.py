from django import forms
from .models import Message, Post, Comment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):
  class Meta:
    model = Post
    fields = "__all__"
    widgets = {
      'title': forms.TextInput(attrs={'class': 'form-control'}),
      'description': forms.Textarea(attrs={'class': 'form-control'})
    }

class MessageForm(forms.ModelForm):
  class Meta:
    model = Message
    fields = "__all__"
    widgets = {
      'body': forms.Textarea(attrs={'class': 'form-control'})
    }      

class CommentForm(forms.ModelForm):
  class Meta:
    model = Comment
    fields = ['description']
    widgets = {
      'description': forms.Textarea(attrs={'class': 'form-control'})
    }

class UserRegisterForm(UserCreationForm):
  class Meta:
    model = User
    fields = ['username', 'email', 'password1', 'password2']