from django.shortcuts import render,redirect,HttpResponse,get_object_or_404,reverse
from post.models import Post,
from django.views import generic
from django.contrib.auth.models import User
from post.forms import CommentForm
from rest_framework import generics
from .serializers import PostSerializer




# Create your views here.








#API

class PostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class =PostSerializer


        
    



