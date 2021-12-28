#!/usr/bin/env python3

from django.urls import path, include
from rest_framework import urlpatterns
from rest_framework.routers import SimpleRouter
from . import views
from rest_framework.authtoken.views import obtain_auth_token

router = SimpleRouter()
router.register('', views.TasksViewSet, basename='taskview')

urlpatterns = [
	path('register/', views.Register.as_view()),
	path('api-token-auth/', obtain_auth_token),
]

urlpatterns += router.urls