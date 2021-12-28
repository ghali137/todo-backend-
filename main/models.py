from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
	title = models.CharField(max_length=100)
	detail = models.TextField()
	user = models.ForeignKey(User, related_name='tasks', on_delete=models.CASCADE)
	
	def __str__(self):
		return f'{self.title}: {self.detail}'
	