from django.urls import path, include
from rest_framework import routers
from user.views import *


user_router = routers.DefaultRouter()
user_router.register("viewset", UserViewSet)

urlpatterns = [
    path('v3/', include(user_router.urls)),
]