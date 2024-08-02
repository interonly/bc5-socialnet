from django.urls import path, include
from rest_framework import routers
from posts.views import *


publication_router = routers.DefaultRouter()
publication_router.register("viewset", PublicationViewSet)

urlpatterns = [
    path('v3/', include(publication_router.urls)),
]