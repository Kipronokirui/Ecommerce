from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class Vendor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=100, null=True, blank=True)
    
    def __str__(self):
        return self.user.username
    
class Category(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField()
    
    def __str__(self):
        return self.title
    
class Product(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField()
    price =  models.DecimalField(max_digits=8, decimal_places=2, default=0.0)
    
    def __str__(self):
        return self.title
