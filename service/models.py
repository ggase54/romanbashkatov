from django.db import models
from django.urls import reverse

class Post(models.Model):

  title = models.CharField(verbose_name="Title", max_length=100)
  description = models.TextField(verbose_name="Description of post", null=True, blank=True)
  image = models.ImageField(verbose_name="Image", null=True, blank=True)
  created_at = models.DateTimeField(verbose_name="Created at", auto_now_add=True)
  updated_at  = models.DateTimeField(verbose_name="Updated at", auto_now=True)

  def __str__(self):
    return f'{self.title}'

  def get_absolute_url(self):
    return reverse('index')

class Comment(models.Model):
  description = models.TextField(verbose_name="Comment", null=True, blank=True)
  post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
  created_at = models.DateTimeField(verbose_name="Created at", auto_now_add=True)

  def __str__(self):
    return f'{self.body}'

  def get_absolute_url(self):
    return reverse('index')

class Message(models.Model):
  title = models.CharField(verbose_name="Subject", max_length=250, null=True, blank=True)
  body = models.TextField(verbose_name="Message")
  email = models.EmailField(verbose_name="Email", max_length=50)

  def __str__(self):
    return f'{self.title}'

  # def get_absolute_url(self):
  #   return reverse('index')