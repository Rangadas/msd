from django.db import models

# Create your models here.
class registrationdb(models.Model):
    Name = models.CharField(max_length=50,null=True,blank=True)
    Email = models.CharField(max_length=100,null=True,blank=True)
    Password = models.CharField(max_length=50, null=True,blank=True)
