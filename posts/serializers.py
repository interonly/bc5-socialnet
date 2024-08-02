from rest_framework import serializers
from .models import Publication


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication
        fields = ['id', 'title', 'content', 'author', 'created_at', 'updated_at']
