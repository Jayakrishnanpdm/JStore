from django.db import models

# Create your models here.
class Products(models.Model):
    title=models.CharField(max_length=20)
    price=models.IntegerField()
    description=models.TextField()
    image=models.ImageField(upload_to='\images')
    priority=models.IntegerField(default=0)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)