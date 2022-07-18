from django.shortcuts import render, redirect
from .models import Post, Comment
from django.views.generic import ListView, DeleteView, CreateView, UpdateView, DetailView

def index(req):
  return render(req, 'index.html')


def about(req):
  return render(req, 'about.html')

class PostsView(ListView):
  model = Post
  template_name = 'index.html'

class DetailViewPost(DetailView):
  model = Post
  template_name = 'detail_post.html'