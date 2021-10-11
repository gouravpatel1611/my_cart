from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import Orders, Product , Contect
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
    product = Product.objects.all
    return render(request, 'shop/cart.html',{'product':product})


def buynow(request):
    product = Product.objects.all
    if request.method=="POST":
        item = request.POST.get('item_jeson', ' ')
        firstName = request.POST.get('firstName',' ')
        lastName = request.POST.get('lastName',' ')
        phone = request.POST.get('phone',' ')
        email = request.POST.get('email',' ')
        address = request.POST.get('address',' ')
        address2 = request.POST.get('address2',' ')
        state = request.POST.get('state',' ')
        dist = request.POST.get('dist',' ')
        zip = request.POST.get('zip',' ')
        save_info = request.POST.get('save_info',' ')
        total_rs = request.POST.get('total_rs')
        orders = Orders(first_name=firstName,last_name=lastName,items=item ,phone=phone,email=email,address1=address ,address2=address2 ,state=state ,city=dist ,pin_code= zip ,address_for_next_time=save_info,total_rs=total_rs)
        orders.save()
        address_list = [item, firstName , lastName , phone, email, address, address2, state, dist, zip, save_info ]
        order = Orders.objects.all
        return render( request, 'shop/order.html',{'order':order})
    else:
        address_list = []
        return render(request, 'shop/bynow.html',{'product':product, 'item_list': address_list})



def order(request):
    order = Orders.objects.all
    return render( request, 'shop/order.html',{'order':order})