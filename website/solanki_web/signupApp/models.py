from django.db import models

# Create your models here.
class Signup(models.Model):
	name =  models.CharField(max_length=20)
	mobile = models.CharField(max_length=10)
	email = models.EmailField(max_length=30)
	password = models.CharField(max_length=40)