from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Student(models.Model):
	BRANCH = (
		('COMP', 'COMP'),
		('IT', 'IT'),
		('EXTC', 'EXTC'),
		('ETRX', 'ETRX'),
		('MCA', 'MCA'),
		('MTECH-CS','MTECH-CS'),
		('MTECH-EXTC','MTECH-EXTC'),
		('PHD-CS','PHD-CS'),
		('PHD-EXTC','PHD-EXTC'),
	)
	is_student = models.BooleanField(default=True)
	user = models.OneToOneField(User,null=True,blank=True,on_delete=models.CASCADE,related_name="student")
	name = models.CharField(max_length=50,null=True)
	phone = models.CharField(max_length=10,null=True,blank=True)
	spitcoin = models.FloatField(default=0)
	email = models.EmailField(null=False)
	profile_pic = models.ImageField(null=True, blank = True)
	year = models.IntegerField(default=1)
	uid = models.CharField(max_length=10,null=True,blank=True)
	branch = models.CharField(max_length=10,null=True,choices=BRANCH)
	dob = models.DateField(null=True)

	def __str__(self):
		return self.name+' ('+self.uid+')'

class Belongs(models.Model):
	user = models.OneToOneField(User,null=True,blank=True,on_delete=models.CASCADE,related_name="belongs")
	is_student = models.BooleanField(default=False)
	is_teacher = models.BooleanField(default = False)	
	is_manager = models.BooleanField(default=False)
	is_committee = models.BooleanField(default = False)


class LostProperty(models.Model):
	owner = models.ForeignKey(Student, on_delete= models.SET_NULL, null=True)
	pic = models.ImageField(null=True)
	item = models.CharField(max_length=50,null=True)
	desc = models.TextField(null=True)
	claim = models.BooleanField(default=False)

class Portfolio(models.Model):
	student = models.ForeignKey(Student, on_delete= models.SET_NULL, null=True)
	intro = models.CharField(max_length=500,null=True)
	about = models.TextField(null=True)
	linkedin = models.URLField(max_length=50,null=True, blank=True)
	github = models.URLField(max_length=50,null=True, blank=True)
	resume_link = models.URLField(max_length=500,null=True, blank=True)
	def __str__(self):
		return str(self.student)


class Academic(models.Model):
	student = models.ForeignKey(Student, on_delete= models.SET_NULL, null=True)
	at1 = models.FloatField(null=True,blank=True,default=0)
	at2 = models.FloatField(null=True,blank=True,default=0)
	at3 = models.FloatField(null=True,blank=True,default=0)
	at4 = models.FloatField(null=True,blank=True,default=0)
	at5 = models.FloatField(null=True,blank=True,default=0)
	at6 = models.FloatField(null=True,blank=True,default=0)
	at7 = models.FloatField(null=True,blank=True,default=0)
	cgpa1 = models.FloatField(null=True,blank=True,default=0)
	cgpa2 = models.FloatField(null=True,blank=True,default=0)
	cgpa3 = models.FloatField(null=True,blank=True,default=0)
	cgpa4 = models.FloatField(null=True,blank=True,default=0)
	cgpa5 = models.FloatField(null=True,blank=True,default=0)
	cgpa6 = models.FloatField(null=True,blank=True,default=0)
	cgpa7 = models.FloatField(null=True,blank=True,default=0)
	cgpa8 = models.FloatField(null=True,blank=True,default=0)
	def __str__(self):
		return str(self.student)

class Subject(models.Model):
	BRANCH = (
		('COMP', 'COMP'),
		('IT', 'IT'),
		('EXTC', 'EXTC'),
		('ETRX', 'ETRX'),
		('MCA', 'MCA'),
		('MTECH-CS','MTECH-CS'),
		('MTECH-EXTC','MTECH-EXTC'),
		('PHD-CS','PHD-CS'),
		('PHD-EXTC','PHD-EXTC'),
	)
	branch = models.CharField(max_length=10,null=True,choices=BRANCH,default='MCA')
	year = models.IntegerField()
	sub1 = models.CharField(max_length=20,default=None,null=True,blank=True)
	sub2 = models.CharField(max_length=20,default=None,null=True,blank=True)
	sub3 = models.CharField(max_length=20,default=None,null=True,blank=True)
	sub4 = models.CharField(max_length=20,default=None,null=True,blank=True)
	sub5 = models.CharField(max_length=20,default=None,null=True,blank=True)
	sub6 = models.CharField(max_length=20,default=None,null=True,blank=True)
	sub7 = models.CharField(max_length=20,default=None,null=True,blank=True)
	def __str__(self):
		return str(self.branch)+' '+str(self.year)

class Feedback(models.Model):
	student = models.ForeignKey(Student, on_delete= models.SET_NULL, null=True)
	subject = models.CharField(max_length=100, null=True,blank=True)
	desc = models.TextField(null=True)
	happy = models.BooleanField(null=True)
	resolved = models.BooleanField(default=False)
	def __str__(self):
		return str(self.student)


##################
#username:  naitik
#password:  naitik123
