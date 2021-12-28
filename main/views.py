from django.contrib.auth.models import User

from rest_framework.permissions import AllowAny
from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import TaskSerializer, UserSerializer
from .models import Task


# Create your views here.
class TasksViewSet(viewsets.ModelViewSet):
	def get_queryset(self):
		return Task.objects.filter(user=self.request.user)
	
	def perform_create(self, serializer):
		serializer.save(user=self.request.user)
		
	serializer_class = TaskSerializer
	
class Register(generics.CreateAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	permission_classes = (AllowAny, )


#class Login(Sign):
#	def post(self, request, format=None):
#		form = AuthenticationForm(request, request.Post)
#		if form.is_valid():
#			token = Token.objects.create(user=form.cleaned_data.get('username'))
#			return Response({'token':token})
#		return Response('Your credentials are invalid')
#	