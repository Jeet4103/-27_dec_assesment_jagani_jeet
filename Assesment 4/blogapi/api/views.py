from django.shortcuts import render
from .models import *
from .serializer import *
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination

class BlogPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 100

class BlogListCreate(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    pagination_class = BlogPagination

class BlogRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer