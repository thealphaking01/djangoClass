from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Person(models.Model):
	fullName = models.CharField(max_length=255, default='')
	phoneNumber=models.CharField(max_length=16, default='')
	points=models.IntegerField(default=0)
	user = models.OneToOneField(User)