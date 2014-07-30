from django.shortcuts import render
from models import Post
# Create your views here.

from rest_framework import viewsets


class PostViewSet(viewsets.ModelViewSet):
    model = Post