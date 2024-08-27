from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from products . models import Products
from. models import Order,Ordered_item
# Create your views here.

@login_required(login_url='account')
def order(request):
    ordered_items=None
    user=request.user.customer_profile
    order,created=Order.objects.get_or_create(owner=user,order_status=Order.CART_STAGE)
    if request.POST:
        id=request.POST.get('id')
        size=request.POST.get('size')
        quantity=int(request.POST.get('quantity'))
        product=Products.objects.get(id=id)
        user=request.user.customer_profile
        order, created=Order.objects.get_or_create(owner=user,order_status=Order.CART_STAGE)
        existing_item=Ordered_item.objects.filter(product=product,quantity=quantity,size=size,order=order).first()
        if existing_item:
            existing_item.quantity=existing_item.quantity+quantity
            existing_item.save()
        else:
            item=Ordered_item.objects.create(product=product,quantity=quantity,size=size,order=order)
    ordered_items=Ordered_item.objects.filter(order=order)
    return render(request,'cart.html',{'ordered_items':ordered_items})
    
def remove(request,id):
    product=Ordered_item.objects.get(id=id)
    product.delete()
    return redirect('order')

def order_confirm(request):
    user=request.user.customer_profile
    order=Order.objects.get(owner=user,order_status=Order.CART_STAGE)
    order.order_status=Order.ORDER_CONFIRMED
    order.save()
    return render(request,'checkout.html')

def previous_orders(request):
    user = request.user.customer_profile
    order_obj = Order.objects.filter(owner=user).exclude(order_status=Order.CART_STAGE)
    previous_ordered_items = Ordered_item.objects.filter(order__in=order_obj)
    return render(request, 'previous_orders.html', {'previous_ordered_items': previous_ordered_items})

