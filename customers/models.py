from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    address=models.TextField()
    phone=models.CharField(max_length=13)
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='customer_profile')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
