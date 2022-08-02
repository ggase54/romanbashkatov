from django.contrib import admin
from .models import Message, Post, Comment

admin.site.register(Post)

admin.site.register(Comment)

admin.site.register(Message)