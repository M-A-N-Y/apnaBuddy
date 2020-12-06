from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Teacher(models.Model):
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


    is_teacher = models.BooleanField(default=True)
    user = models.OneToOneField(User,null=True,blank=True,on_delete=models.CASCADE,related_name="teacher")
    name = models.CharField(max_length=50,null=True)
    phone = models.CharField(max_length=10,null=True,blank=True)
    spitcoin = models.FloatField(default=0)
    email = models.EmailField(null=False)
    profile_pic = models.ImageField(null=True, blank = True)
    uid = models.CharField(max_length=10,null=True,blank=True)
    branch = models.CharField(max_length=10,null=True,choices=BRANCH)
    dob = models.DateField(null=True)
    password = models.CharField(max_length=50,null=True)

    def __str__(self):
        return self.name+' ('+self.uid+')'
