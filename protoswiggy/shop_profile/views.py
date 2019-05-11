from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse,HttpResponseRedirect
from customer_register.models import UserProfile
from shopadmin.models import Units,Categories,Product 
from shop_register.models import Shop
from product_management.models import Order

# Create your views here.
@login_required
def index(request):
    user = request.user
    info = Shop.objects.get(user=user)
    units = Units.objects.order_by('id')
    categories = Categories.objects.order_by('id')
    products = Product.objects.filter(shop_name=info)
    orders = Order.objects.filter(product__shop_name__shop_name = info).order_by('-order_time')
    context = {
        'user':user,
        'info':info,
        'units':units,
        'categories':categories,
        'products':products,
        'orders':orders,
    }
    return render(request,'shop_profile/index.html',context)

@login_required
def productupdate(request):
    if request.method == 'POST' and request.POST['submit']=='ADD':
        P = Product()
        P.product_name = request.POST['product_name']
        P.rate = request.POST['product_rate']
        P.product_date = request.POST['date']
        P.product_approved = "ON TIME"
        user = request.user
        P.shop_name = Shop.objects.get(user=user)
        P.save()
        return HttpResponseRedirect(reverse('shop_profile:index'))

    if request.method == 'POST' and request.POST['submit']=='DELETE':
        P = Product.objects.get(id=request.POST['product_id'])
        P.delete()
        return HttpResponseRedirect(reverse('shop_profile:index'))

    if request.method == 'POST' and request.POST['submit']=='DELAY':
        P = Product.objects.get(id=request.POST['product_id'])
        P.product_approved = 'DELAY'
        P.save()
        return HttpResponseRedirect(reverse('shop_profile:index'))

@login_required
def orderupdate(request,order_id):
    order = Order.objects.get(id = order_id)
    if request.method == "POST" and request.POST['submit']=='Cancel':
        order.order_status = 'CANCELLED'
        order.save()
        return HttpResponseRedirect(reverse('shop_profile:index'))
    elif request.method == "POST" and request.POST['submit']=='Delivered':
        order.order_status = 'DELIVERED'
        order.save()
        return HttpResponseRedirect(reverse('shop_profile:index'))
    elif request.method == "POST" and request.POST['submit']=='Confirm':
        order.order_status = 'CONFIRMED'
        order.save()
        return HttpResponseRedirect(reverse('shop_profile:index'))

