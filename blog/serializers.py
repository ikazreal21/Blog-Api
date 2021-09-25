from rest_framework import serializers
from .models import *


class PostSerializer(serializers.ModelSerializer):
    comment = serializers.StringRelatedField(many=True)

    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'body',
            'status',
            'author',
            'ranid',
            'comment',
            'image',
        ]


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ['id', 'user', 'comment', 'post', 'ranid']
