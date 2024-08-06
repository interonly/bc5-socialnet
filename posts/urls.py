from django.urls import path, include
from rest_framework import routers
from posts.views import *


publication_router = routers.DefaultRouter()
publication_router.register("viewset", PublicationViewSet)

like_router = routers.DefaultRouter()
like_router.register("like", LikeViewSet)

dislike_router = routers.DefaultRouter()
dislike_router.register("dislike", DislikeViewSet)

urlpatterns = [
    path('publication/', include(publication_router.urls)),
    path('rating/', include(like_router.urls)),
    path('rating/', include(dislike_router.urls)),
]