from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse,HttpResponseRedirect
from customer_register.models import UserProfile
from shop_register.models import Shop
from product_management.models import Order 
# Create your views here.

@login_required
def index(request):
    user = request.user
    info = UserProfile.objects.get(user=user)
    orders = Order.objects.filter(customer__user=user)
    context = {
        'user':user,
        'u':info,
        'orders':orders
    }
    return render(request,'customer_profile/index.html',context)

@login_required
def ordercancel(request, order_id):
    order = Order.objects.get(id=order_id)
    order.order_status="CANCELLED"
    order.save()
    return HttpResponseRedirect(reverse('customerprofile:index'))