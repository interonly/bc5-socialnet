from django.urls import path, include
from rest_framework import routers
from comments.views import *


comment_router = routers.DefaultRouter()
comment_router.register("viewset", CommentViewSet)

urlpatterns = [
    path('v3/', include(comment_router.urls)),
]