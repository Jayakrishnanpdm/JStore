from django.shortcuts import render
from . models import Products
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    return render(request,'home_layout.html')

def products(request):
    page=1
    if request.GET:
        page=request.GET.get('page',1)    
    product_list=Products.objects.all()
    paginator=Paginator(product_list,3)
    page_list=paginator.get_page(page)
    return render(request,'products.html',{"product_list":page_list})


def product_detail(request):
    return render(request,'product_detail.html')


