from django.db import models

# Create your models here.

class Manager(models.Model):
	name = models.CharField(max_length=50,null=True)
	phone = models.CharField(max_length=10,null=True)
	balance = models.FloatField(default=0)
	email = models.EmailField(null=False)
	profile_pic = models.ImageField(null=True)

class Menu(models.Model):
	CAT = (
			('lunch', 'lunch'),
			('breakfast', 'breakfast'),
			('snack', 'snack'),
			) 
	name = models.CharField(max_length=50,null=True)
	price = models.FloatField(default=0)
	pic = models.ImageField(null=True)
	category = models.CharField(max_length=50,null=True,choices=CAT)

class Order(models.Model):
	#onum = models.AutoField()
	#customer = models.ForeignKey(Student, on_delete= models.SET_NULL, null=True)
	canteen = models.ForeignKey(Manager, on_delete= models.SET_NULL, null=True)
	item = models.ForeignKey(Menu,on_delete=models.SET_NULL,null=True)
	delivered = models.BooleanField(default=False)
