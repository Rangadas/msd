from django.db import models

# Create your models here.
class catdb(models.Model):
    Name = models.CharField(max_length=50,null=True,blank=True)
    Description = models.CharField(max_length=500,null=True,blank=True)
    Image = models.ImageField(upload_to="Profile")
class productdb(models.Model):
    CategoryName = models.CharField(max_length=50,null=True,blank=True)
    ProductName = models.CharField(max_length=50,null=True,blank=True)
    Description = models.CharField(max_length=500, null=True, blank=True)
    Quantity = models.IntegerField(null=True,blank=True)
    Price = models.IntegerField(null=True,blank=True)
    Image = models.ImageField(upload_to="Profile",null=True)
class messagedb(models.Model):
    Name = models.CharField(max_length=50,null=True,blank=True)
    Email = models.EmailField(max_length=50,null=True,blank=True)
    Mobile = models.IntegerField(null=True,blank=True)
    Message = models.CharField(max_length=500,null=True,blank=True)

