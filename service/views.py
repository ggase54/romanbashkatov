from django.shortcuts import render
from .models import Post, Comment
from django.views.generic import ListView, DeleteView, CreateView, UpdateView, DetailView
from .forms import PostForm, CommentForm, UserRegisterForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

@login_required
def about(req):
  return render(req, 'about.html')

class PostsView(ListView):
  model = Post
  template_name = 'index.html'
  ordering = ['created_at']

class RegisterForm(CreateView, LoginRequiredMixin):
  form_class = UserRegisterForm
  template_name = 'register.html'
  success_url = reverse_lazy('login')

class DetailPostView(DetailView):
  model = Post
  template_name = 'detail_post.html'

class CreatePostView(CreateView, LoginRequiredMixin):
  model = Post
  template_name = 'create_post.html'
  form_class = PostForm

class UpdatePostView(UpdateView, LoginRequiredMixin):
  model = Post 
  template_name = 'update_post.html'
  form_class  = PostForm

class DeletePostView(DeleteView, LoginRequiredMixin):
  model = Post 
  template_name = 'delete_post.html'
  success_url = reverse_lazy('index')

class AddCommentView(CreateView, LoginRequiredMixin):
  model = Comment 
  template_name = 'add_comment.html'
  form_class = CommentForm

  def form_valid(self, form):
    form.instance.post_id = self.kwargs['pk']
    return super().form_valid(form)