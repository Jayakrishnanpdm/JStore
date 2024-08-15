from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home_layout.html')

def products(request):
    return render(request,'products.html')

def product_detail(request):
    return render(request,'home_layout.html')

def product_detail(request):
    return render(request,'product_detail.html')

def account(request):
    return render(request,'account.html')

def cart(request):
    return render(request,'cart.html')