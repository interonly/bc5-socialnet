from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Publication


class PostSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='author.username', read_only=True)

    class Meta:
        model = Publication
        fields = ['title', 'content', 'author', 'created_at', 'updated_at']