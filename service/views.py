# from django.conf import settings
from django.shortcuts import redirect, render
from .models import Post, Comment
from django.views.generic import ListView, DeleteView, CreateView, UpdateView, DetailView
from .forms import MessageForm, PostForm, CommentForm, UserRegisterForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required, permission_required
from django.core.mail import send_mail

def about(req):
  form = MessageForm()
  if req.method == "POST":
    form = MessageForm(req.POST)
    if form.is_valid():
      subject = form.cleaned_data.get("title")
      body = form.cleaned_data.get("body")
      email = form.cleaned_data.get("email")
      send_mail(
      subject, body, 'testggase@yandex.com', [email], fail_silently=False
        )
      return redirect('index')
  return render(req, 'about.html', {'form': form})

class PostsView(ListView):
  model = Post
  template_name = 'index.html'
  ordering = ['created_at']

class RegisterForm(SuccessMessageMixin, CreateView):
  form_class = UserRegisterForm
  success_message = "%(username)s was created successfully!"
  template_name = 'register.html'
  success_url = reverse_lazy('login')

class DetailPostView(DetailView):
  model = Post
  template_name = 'detail_post.html'

# class CreatePostView(PermissionRequiredMixin, CreateView):
#   permission_required = 'service.add_post'
#   model = Post
#   template_name = 'create_post.html'
#   form_class = PostForm

@login_required
@permission_required('service.add_post')
def create_post(req):
  form = PostForm()
  if req.method == 'POST':
    form = PostForm(req.POST)
    if form.is_valid():
      form.save()
      title = form.cleaned_data.get("title")
      if title == 'post' or title == 'POST' or title == 'Post':
        messages.error(req, f"Something went wrong.")
        return redirect('index')
      else:
        messages.success(req, f"{title} was created successfully!")
      return redirect('index')
  return render(req, 'create_post.html', {'form': form})


class UpdatePostView(PermissionRequiredMixin, UpdateView):
  permission_required = 'service.update_post'
  model = Post 
  template_name = 'update_post.html'
  form_class  = PostForm

class DeletePostView(PermissionRequiredMixin, DeleteView):
  permission_required = 'service.delete_post'
  model = Post 
  template_name = 'delete_post.html'
  success_url = reverse_lazy('index')

class AddCommentView(LoginRequiredMixin, CreateView):
  model = Comment 
  template_name = 'add_comment.html'
  form_class = CommentForm

  def form_valid(self, form):
    form.instance.post_id = self.kwargs['pk']
    return super().form_valid(form)