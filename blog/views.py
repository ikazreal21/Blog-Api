from rest_framework import generics
from .models import *
from .serializers import *


class PostList(generics.ListCreateAPIView):
    queryset = Post.pubpost.all()
    serializer_class = PostSerializer


class PostDraft(generics.ListAPIView):
    queryset = Post.draftpost.all()
    serializer_class = PostSerializer


class PostDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
