from django.db import models
from customers import Customer
from products import Products

# Create your models here.

class Order(models.Model):
    CART_STAGE=0
    ORDER_CONFIRMED=1
    ORDER_PROCESSED=2
    ORDER_DELIVERED=3
    ORDER_REJECTED=4
    status_choice=(('CART_STAGE',CART_STAGE),
                   ('ORDER_CONFIRMED',ORDER_CONFIRMED),
                   ('ORDER_DELIVERED',ORDER_DELIVERED),
                   ('ORDER_REJECTED',ORDER_REJECTED)
                   )
    order_status=models.IntegerField(choices=status_choice,default=CART_STAGE)
    owner=models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True,related_name='orders')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class Ordered_item(models.Model):
    product=models.ForeignKey(Products,on_delete=models.CASCADE,related_name='orders')
    quantity=models.IntegerField(default=1)
    size=models.CharField(max_length=10)
    order=models.ForeignKey(Order,on_delete=models.CASCADE,related_name='add_to_cart')

