from operator import mod
from statistics import mode
from django.db import models


# Create your models here.
class Student(models.Model):
	adm_mode = models.CharField(max_length=20)
	sid = models.CharField(max_length=20)
	adm_date = models.DateField()
	category = models.CharField(max_length=2)
	branch = models.CharField(max_length=10)
	sname = models.CharField(max_length=50)
	sdob = models.DateField()
	quota = models.CharField(max_length=20)
	tneanum = models.CharField(max_length=30)
	admquota = models.CharField(max_length=20)
	firstgrad = models.CharField(max_length=10)
	tnscst = models.CharField(max_length=20)
	tnbc = models.CharField(max_length=20)
	aicte = models.CharField(max_length=20)
	sgender = models.CharField(max_length=10)
	medium = models.CharField(max_length=30)
	nationality = models.CharField(max_length=30)
	religion = models.CharField(max_length=30)
	community = models.CharField(max_length=30)
	caste = models.CharField(max_length=30)
	bloodgroup = models.CharField(max_length=10)
	saadhar = models.CharField(max_length=30)
	smobilenum = models.CharField(max_length=30)
	smail = models.CharField(max_length=50)
	scolmode = models.CharField(max_length=30)
	phychallenged = models.CharField(max_length=10)
	fathername = models.CharField(max_length=30)
	mothername = models.CharField(max_length=30)
	guardianname = models.CharField(max_length=30)
	comaddress = models.CharField(max_length=100)
	permaddress = models.CharField(max_length=100)
	state = models.CharField(max_length=30)

	class Meta:
		db_table="detail"