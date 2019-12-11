from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from example import views

from example.views import CustomAuthToken

urlpatterns = [
    re_path(r'^', views.CustomAuthToken.as_view()),
    re_path(r'^/adduser/$', views.UsersList.as_view()),
]