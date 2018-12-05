from django.db import models

# Create your models here.
class Users(models.Model): 
	userID = models.CharField(max_length = 30)
	userName = models.CharField(max_length = 250)

	#override 
	def __str__(self):
		return self.userID + ' - ' + self.userName

class Business(models.Model): 
	business_id = models.CharField(max_length = 100) 
	name = models.CharField(max_length = 50) 
	avg_stars = models.CharField(max_length = 3)
	categories = models.CharField(max_length = 200)

	def __str__(self):
		return self.name 

class Reviews(models.Model): 
	business_id = models.ForeignKey(Business, on_delete=models.CASCADE) 
	text = models.CharField(max_length = 100) 
	stars = models.CharField(max_length = 3)
	prediction = models.CharField(max_length = 3) 
	userID = models.ForeignKey(Users, on_delete=models.CASCADE)
	review_id = models.CharField(max_length = 30, default = "", editable=False) 

	def __str__(self):
		return self.review_id 
	