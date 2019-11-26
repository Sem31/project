from django.db import models

class Signup(models.Model):
	first_name = models.CharField(max_length=20)
	email    = models.EmailField(max_length=254)
	user_name = models.CharField(max_length=50)
	contact  = models.CharField(max_length=10)
	password = models.CharField(max_length=50)


	def __str__(self):
		return self.first_name


class Login(models.Model):
	email = models.CharField(max_length=50)
	pasword = models.CharField(max_length=50)

	def __str__(self):
		return self.email
	