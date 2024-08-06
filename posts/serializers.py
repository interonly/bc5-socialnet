from rest_framework import serializers
from .models import *


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication
        fields = ['id', 'title', 'content', 'author', 'created_at', 'updated_at']


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['post', 'user', 'created_at', 'updated_at']
        