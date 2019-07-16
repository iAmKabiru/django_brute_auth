from django.db import models

class Authentication(models.Model):
	username = models.CharField(max_length=25)
	password = models.CharField(max_length=16)

class Users(models.Model):
	first_name = models.CharField(max_length=20)
	last_name = models.CharField(max_length=20)
	address = models.CharField(max_length=30)

	def get_full_name(self):
		return "{} {}".format(self.first_name, self.last_name)


