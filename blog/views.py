from rest_framework import generics
from .models import *
from .serializers import *
from rest_framework.permissions import (
    IsAdminUser,
    DjangoModelPermissionsOrAnonReadOnly,
    BasePermission,
    SAFE_METHODS,
)


class AuthorWritePermission(BasePermission):
    message = "Only the Author is Allowed to edit this."

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user


class AuthorWriteCommentPermission(BasePermission):
    message = "Only the Author is Allowed to edit this Comment"

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.user == request.user


class PostList(generics.ListCreateAPIView):
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    queryset = Post.pubpost.all()
    serializer_class = PostSerializer


class PostDraft(generics.ListAPIView):
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    queryset = Post.draftpost.all()
    serializer_class = PostSerializer


class PostDetails(generics.RetrieveUpdateDestroyAPIView, AuthorWritePermission):
    permission_classes = [AuthorWritePermission]
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CommentList(generics.ListCreateAPIView):
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer


class CommentDetails(
    generics.RetrieveUpdateDestroyAPIView, AuthorWriteCommentPermission
):
    permission_classes = [AuthorWriteCommentPermission]
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer
