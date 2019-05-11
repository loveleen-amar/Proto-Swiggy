from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse,HttpResponseRedirect
from customer_register.models import UserProfile
from shop_register.models import Shop
from shopadmin.models import Product, Categories, Units
from django.utils import timezone
from .models import Order
# Create your views here.
def index(request,product_id):
    product = Product.objects.get(id=product_id)
    context = {
        'product':product,
    }
    return render(request,'product_management/index.html',context)


def product_order(request,product_id):
    user = request.user
    if user is not None:
        try:
            order = Order()
            order.product = Product.objects.get(id=product_id)
            customer = UserProfile.objects.get(user=request.user)
            order.customer = customer
            order.order_status = "PENDING"
            order.quantity = request.POST['quantity']
            order.total_cost = int(order.product.rate)*int(order.quantity)
            order.order_time = timezone.now()
            order.save()
            return render(request,'product_management/order_confirmed.html')
        except:
            return HttpResponseRedirect(reverse('login_app:index'))
    else:
        return HttpResponseRedirect(reverse('login_app:index'))
