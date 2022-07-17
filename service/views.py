from django.shortcuts import render, redirect
from .models import Post, Comment

def index(req):
  return render(req, 'index.html')


def about(req):
  return render(req, 'about.html')