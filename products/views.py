from django.shortcuts import render
from . models import Products
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    product_list_featured = Products.objects.filter(priority__range=(1, 4))
    product_list_latest=Products.objects.exclude(id=23).order_by('-id')[:4]
    return render(request,'home_layout.html',{'product_list_featured':product_list_featured,'product_list_latest':product_list_latest})

def products(request):
    page=1
    if request.GET:
        page=request.GET.get('page',1)    
    product_list=Products.objects.all().exclude(id=23)
    paginator=Paginator(product_list,4)
    page_list=paginator.get_page(page)
    return render(request,'products.html',{"product_list":page_list})


def product_detail(request,id):
    product=Products.objects.get(id=id)
    title=product.title
    related_products = Products.objects.filter(title=title).exclude(id=id)
    return render(request,'product_detail.html',{"product":product,"related_products":related_products})


