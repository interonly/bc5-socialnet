from rest_framework import viewsets
from posts.models import *
from posts.serializers import *


class PublicationViewSet(viewsets.ModelViewSet):
    queryset = Publication.objects.all()
    serializer_class = PostSerializer

class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = RatingSerializer

class DislikeViewSet(viewsets.ModelViewSet):
    queryset = Dislike.objects.all()
    serializer_class = RatingSerializer
