from django.urls import path
from user.views import *


urlpatterns = [
    path("list/", UserList.as_view(), name="user-list"),
    path('info/<int:pk>/', UserInfo.as_view())
]