from django.db import models

# Create your models here.

class Authentication(models.Model):
    emailid = models.EmailField(max_length=100)
    password= models.CharField(max_length=200,blank=False, default='')
    


