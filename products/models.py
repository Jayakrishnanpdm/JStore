from django.db import models
from customers.models import Customer

# Create your models here.
class Products(models.Model):
    title=models.CharField(max_length=20)
    price=models.IntegerField()
    description=models.TextField()
    image=models.ImageField(upload_to='media/')
    priority=models.IntegerField(default=0)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class ProductReview(models.Model):    
    content=models.CharField(max_length=30)
    user=models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True,related_name='review')
    product=models.ForeignKey(Products,on_delete=models.CASCADE,related_name='review')