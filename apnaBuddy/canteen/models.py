from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Manager(models.Model):
	is_manager = models.BooleanField(default=True)
	user = models.OneToOneField(User,null=True,blank=True,on_delete=models.CASCADE,related_name="manager")
	name = models.CharField(max_length=50,null=True)
	phone = models.CharField(max_length=10,null=True)
	balance = models.FloatField(default=0)
	email = models.EmailField(null=False)
	profile_pic = models.ImageField(null=True, blank = True)

	def __str__(self):
		return self.name


class Menu(models.Model):
	CAT = (
			('lunch', 'lunch'),
			('breakfast', 'breakfast'),
			('snack', 'snack'),
			)
	name = models.CharField(max_length=50,null=True)
	price = models.FloatField(default=0)
	pic = models.ImageField(null=True,blank = True)
	category = models.CharField(max_length=50,null=True,choices=CAT)

	def __str__(self):
		return self.name


class Order(models.Model):
	#onum = models.AutoField()
	#customer = models.ForeignKey(Student, on_delete= models.SET_NULL, null=True)
	canteen = models.ForeignKey(Manager, on_delete= models.SET_NULL, null=True)
	item = models.ForeignKey(Menu,on_delete=models.SET_NULL,null=True)
	delivered = models.BooleanField(default=False)
	# def __str__(self):
	# 	return self.name
