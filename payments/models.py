from django.db import models
from orders.models import Order

# Create your models here.
class PaymentStatus(models.Model):
    mode=models.CharField(max_length=20)
    order=models.OneToOneField(Order,on_delete=models.CASCADE,related_name="payment",null=True)