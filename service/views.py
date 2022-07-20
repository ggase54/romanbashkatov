from django.shortcuts import render
from .models import Post, Comment
from django.views.generic import ListView, DeleteView, CreateView, UpdateView, DetailView
from .forms import PostForm, CommentForm
from django.urls import reverse_lazy

def about(req):
  return render(req, 'about.html')

class PostsView(ListView):
  model = Post
  template_name = 'index.html'
  ordering = ['created_at']

class DetailPostView(DetailView):
  model = Post
  template_name = 'detail_post.html'

class CreatePostView(CreateView):
  model = Post
  template_name = 'create_post.html'
  form_class = PostForm

class UpdatePostView(UpdateView):
  model = Post 
  template_name = 'update_post.html'
  form_class  = PostForm

class DeletePostView(DeleteView):
  model = Post 
  template_name = 'delete_post.html'
  success_url = reverse_lazy('index')

class AddCommentView(CreateView):
  model = Comment 
  template_name = 'add_comment.html'
  form_class = CommentForm

  def form_valid(self, form):
    form.instance.post_id = self.kwargs['pk']
    return super().form_valid(form)