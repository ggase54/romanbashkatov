import csv
import datetime

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
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse

@login_required
def about(req):
    form = MessageForm()
    if req.method == "POST":
        form = MessageForm(req.POST)
        if form.is_valid():
            subject = form.cleaned_data.get("title")
            body = form.cleaned_data.get("body")
            email = form.cleaned_data.get("email1")
            email_2 = form.cleaned_data.get("email2")
            send_mail(
            subject, body, 'testggase@yandex.com', [email, email_2], fail_silently=False
                )
            return redirect('index')
    return render(req, 'about.html', {'form': form})

class PostsView(ListView):
  model = Post
  template_name = 'index.html'
  ordering = ['-created_at']

class RegisterForm(SuccessMessageMixin, CreateView):
  form_class = UserRegisterForm
  success_message = "%(username)s was created successfully!"
  template_name = 'register.html'
  success_url = reverse_lazy('login')

class DetailPostView(DetailView):
  model = Post
  template_name = 'detail_post.html'

class CreatePostView(SuccessMessageMixin, PermissionRequiredMixin, CreateView):
  form_class = PostForm
  success_message = "%(title)s was created successfully!"
  template_name = 'create_post.html'
  model = Post
  permission_required = 'service.create_post'
  success_url = reverse_lazy('index')

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

def upload(req):
    context = {}
    if req.method == "POST":
        uploaded_file = req.FILES['file']
        file = FileSystemStorage()
        name = file.save(uploaded_file.name, uploaded_file)
        context['url'] = file.url(name)
        # return redirect('index')
    return render(req, "upload.html", context)

def download(req):
    responce = HttpResponse(content_type='text/csv')
    writer = csv.writer(responce)
    writer.writerow(['Title', 'Description', 'Created_at'])
    
    for row in Post.objects.all().values_list('title', 'description', 'created_at'):
        writer.writerow(row)
    
    filename = str(datetime.datetime.now()) + 'posts.csv'
    responce['Content-Disposition'] = f"attachment; filename={filename}"
    return responce