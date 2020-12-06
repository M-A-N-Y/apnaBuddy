from django.db import models

# Create your models here.
class Student(models.Model):
	BRANCH = (
		('COMP', 'COMP'),
		('IT', 'IT'),
		('EXTC', 'EXTC'),
		('ETRX', 'ETRX'),
		('MCA', 'MCA'),
		) 
	name = models.CharField(max_length=50,null=True)
	phone = models.CharField(max_length=10,null=True)
	spitcoin = models.FloatField(default=0)
	email = models.EmailField(null=False)
	profile_pic = models.ImageField(null=True)
	year = models.IntField(default=1)
	uid = models.CharField(max_length=10,null=True)
	branch = models.CharField(max_length=10,null=True,choices=BRANCH)
	dob = models.DateField(null=True)




class LostPropery(models.Model):
	owner = models.ForeignKey(Student, on_delete= models.SET_NULL, null=True)
	pic = models.ImageField(null=True)
	item = models.CharField(max_length=50,null=True)
	desc = models.TextField(null=True)
	claim = models.BooleanField(default=False)
	finder = models.ForeignKey(Student, on_delete= models.SET_NULL, null=True)

class Portfolio(models.Model):
	student = models.ForeignKey(Student, on_delete= models.SET_NULL, null=True)
	intro = models.CharField(max_length=500,null=True)
	about = models.TextField(null=True)
	linkedin = models.CharField(max_length=50,null=True) 
	github = models.CharField(max_length=50,null=True) 
	resume_link = models.CharField(max_length=500,null=True) 

class Academic(models.Model):
	student = models.ForeignKey(Student, on_delete= models.SET_NULL, null=True)
	at1 = models.FloatField(null=True) 
	at2 = models.FloatField(null=True) 
	at3 = models.FloatField(null=True) 
	at4 = models.FloatField(null=True) 
	at5 = models.FloatField(null=True) 
	at6 = models.FloatField(null=True) 
	at7 = models.FloatField(null=True) 
	cgpa1 = models.FloatField(null=True) 
	cgpa2 = models.FloatField(null=True) 
	cgpa3 = models.FloatField(null=True) 
	cgpa4 = models.FloatField(null=True) 
	cgpa = models.FloatField(null=True) 


class Subject(models.Model):
	year = models.IntegerField(default=1)
	sub1 = models.FloatField(null=True) 
	sub2 = models.FloatField(null=True) 
	sub3 = models.FloatField(null=True) 
	sub4 = models.FloatField(null=True) 
	sub5 = models.FloatField(null=True) 
	sub6 = models.FloatField(null=True) 
	sub7 = models.FloatField(null=True)	

class Feedback(models.Model):
	student = models.ForeignKey(Student, on_delete= models.SET_NULL, null=True)
	desc = models.TextField(null=True)
	happy = models.BooleanField(null=True)

