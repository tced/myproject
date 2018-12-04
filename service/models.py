from django.db import models

# Create your models here.
class Users(models.Model): 
	userID = models.CharField(max_length = 30)
	userName = models.CharField(max_length = 250)

	def __str__(self):
		return self.userID + ' - ' + self.userName