#!/usr/bin/env python3

from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Task
from rest_framework.authtoken.models import Token


class TaskSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Task
		fields = ['pk', 'title', 'detail']
		

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('username', 'password')
		extra_kwargs = {'password': {'write_only': True}}
		
	def create(self, validated_data):
		password = validated_data.pop('password')
		user = User(**validated_data)
		user.set_password(password)
		user.save()
		return user