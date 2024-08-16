from django.shortcuts import render
from . models import Products
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    return render(request,'home_layout.html')

def products(request):
    product_list=Products.objects.all()
    paginator=Paginator(product_list,3)
    page=paginator.get_page(1)
    return render(request,'products.html',{"product_list":page})


def product_detail(request):
    return render(request,'product_detail.html')


