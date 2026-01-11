from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    phone = models.CharField(max_length=15, blank=True,null=True)


class Product(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=100,blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
