from django.db import models
from django.utils import timezone

class Committee(models.Model) :
	name = models.CharField(max_length = 100)
	about = models.TextField(max_length = 100)
	icon = models.ImageField(null=True)
	email = models.EmailField(null=False)
	linkedin = models.URLField(max_length=50,null=True, blank=True)
	instagram = models.URLField(max_length=50,null=True, blank=True) 
	balance = models.FloatField(default = 0)
	def __str__(self):
		return str(self.name)

class Events(models.Model) :
	name = models.ForeignKey(Committee, on_delete= models.CASCADE, null=True)
	headline = models.TextField(max_length = 100)
	dop = models.DateTimeField(default = timezone.now)
	cost = models.FloatField(default = 0)
	regLink = models.URLField(max_length = 200)
	def __str__(self):
		return str(self.name)

