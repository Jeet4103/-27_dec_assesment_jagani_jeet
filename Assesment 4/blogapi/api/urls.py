from django.contrib import admin
from django.urls import path, include
from .views import BlogListCreate, BlogRetrieveUpdateDestroy

urlpatterns = [
    path('blogs/', BlogListCreate.as_view(), name='blog-list-create'),
    path('blogs/<int:pk>/', BlogRetrieveUpdateDestroy.as_view(), name='blog-retrieve-update-destroy'),
]