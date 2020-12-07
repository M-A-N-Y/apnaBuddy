from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from student.models import Student

class Committee(models.Model) :
	is_committee = models.BooleanField(default=True)
	user = models.OneToOneField(User,null=True,blank=True,on_delete=models.CASCADE,related_name="committee")
	name = models.CharField(max_length = 100)
	about = models.TextField(max_length = 100)
	icon = models.ImageField(null=True, blank = True)
	email = models.EmailField(null=False)
	linkedin = models.URLField(max_length=50,null=True, blank=True)
	instagram = models.URLField(max_length=50,null=True, blank=True)
	balance = models.FloatField(default = 0)
	def __str__(self):
		return str(self.name)

class Events(models.Model) :
	name = models.ForeignKey(Committee, on_delete= models.CASCADE, null=True)
	headline = models.TextField(max_length = 100)
	desc = models.TextField(max_length = 2000, default='')
	dop = models.DateTimeField(default = timezone.now)
	cost = models.FloatField(default = 0)
	regLink = models.URLField(max_length = 200)
	paid = models.ManyToManyField(Student, null=True,blank=True)
	def __str__(self):
		return str(self.name)

