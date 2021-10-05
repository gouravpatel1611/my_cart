from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import Product , Contect
from math import *

# Create your views here.

def index(request): 
    all_product = []
    cat_product = Product.objects.values('category')
    cats = {item['category'] for item in cat_product}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = ceil(n/4)
        all_product.append([prod, range(1,nSlides),nSlides]),
    params = {'all_product': all_product}
    return render(request, 'shop/index.html', params)

def about(request):
    return render(request, 'shop/about.html')

def contect(request):
    if request.method=="POST":
        fname = request.POST.get('fname',' ')
        lname = request.POST.get('lname',' ')
        email = request.POST.get('email',' ')
        comment = request.POST.get('comment',' ')
        contect = Contect(fname=fname, lname=lname, email=email, comment=comment)
        contect.save()
        print(fname, lname, email, comment)
        
    return render(request , 'shop/contectas.html')

def tracker(request):
    return render(request, 'shop/tracker.html')


def product_view(request , my_id):
    product = Product.objects.filter(id = my_id)
    return render(request, 'shop/product.html', {'product':product})

def cart(request):
    return render(request, 'shop/cart.html')