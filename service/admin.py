from django.contrib import admin
from .models import Message, Post, Comment

class PostAdmin(admin.ModelAdmin):
  list_display = ['title', 'description']
  fields = (('title', 'description'), 'image')
  search_fields = ['title']
admin.site.register(Post, PostAdmin)

class CommentAdmin(admin.ModelAdmin):
  list_display = ['description']
  list_filter = ['description']
admin.site.register(Comment, CommentAdmin)

admin.site.register(Message)