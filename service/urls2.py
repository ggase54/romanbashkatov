from unicodedata import name
from service import views
from django.urls import path

urlpatterns = [
  path('', views.PostsView.as_view(), name='index'),
  path('post/<int:pk>', views.DetailViewPost.as_view(), name='detail_post'),
  path('about/', views.about, name='about'),
  ]