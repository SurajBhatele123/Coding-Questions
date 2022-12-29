from django.db import models

# Create your models here.
class Employee(models.Model):
    firstname=models.CharField(max_length=45,blank=False, default='')
    lastname=models.CharField(max_length=45,blank=False, default='')
    dob=models.DateField(blank=False,default='')
    gender=models.CharField(max_length=7,blank=False, default='')
    emailid=models.CharField(max_length=45,blank=False, default='')
    mobile=models.CharField(max_length=12,blank=False, default='')
    address=models.CharField(max_length=200,blank=False, default='')
    state=models.CharField(max_length=45,blank=False, default='')
    city=models.CharField(max_length=45,blank=False, default='')
    designation=models.CharField(max_length=45,blank=False, default='')
    managerid=models.IntegerField(blank=False)
    photograph=models.ImageField(upload_to='static/')
    
class States(models.Model):
    stateid=models.IntegerField(blank=False)
    statename=models.CharField(max_length=45,blank=False, default='')
    
class Cities(models.Model):
    stateid=models.IntegerField(blank=False)
    cityid=models.IntegerField(blank=False)
    cityname=models.CharField(max_length=45,blank=False, default='')

class Manager(models.Model):
    managerid=models.IntegerField(blank=False)
    firstname=models.CharField(max_length=45,blank=False, default='')
    lastname=models.CharField(max_length=45,blank=False, default='')
    dob=models.DateField(blank=False,default='')
    gender=models.CharField(max_length=7,blank=False, default='')
    emailid=models.CharField(max_length=45,blank=False, default='')
    mobile=models.CharField(max_length=12,blank=False, default='')
    address=models.CharField(max_length=200,blank=False, default='')
    state=models.CharField(max_length=45,blank=False, default='')
    city=models.CharField(max_length=45,blank=False, default='')
    photograph=models.ImageField(upload_to='static/')
    
class Customer(models.Model):
    firstname=models.CharField(max_length=45,blank=False, default='')
    lastname=models.CharField(max_length=45,blank=False, default='')
    dob=models.DateField(blank=False,default='')
    gender=models.CharField(max_length=7,blank=False, default='')
    emailid=models.CharField(max_length=45,blank=False, default='')
    organizationname=models.CharField(max_length=45,blank=False, default='')
    mobile=models.CharField(max_length=12,blank=False, default='')
    alternatemobile=models.CharField(max_length=12,blank=False, default='')
    address=models.CharField(max_length=200,blank=False, default='')
    state=models.CharField(max_length=45,blank=False, default='')
    city=models.CharField(max_length=45,blank=False, default='')
    photograph=models.ImageField(upload_to='static/')