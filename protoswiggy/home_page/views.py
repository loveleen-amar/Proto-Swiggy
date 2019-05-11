from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse,HttpResponseRedirect
from customer_register.models import UserProfile
from shop_register.models import Shop
from shopadmin.models import Categories,Units,Product
import datetime
import dateutil.parser
from django.utils import timezone
# Create your views here.
def home_view(request):
    categories = Categories.objects.order_by('id')
    context = {
        'categories':categories,
    }
    return render(request,'home_page/index.html',context)


def search(request):
    data = request.POST['date']
    data = list(data.split('-'))
    year = int(data[0])
    month = int(data[1])
    date = int(data[2])
    products = Product.objects.filter(product_date__lte = datetime.date(year,month,date))

    context = {
        'products':products,
    }
    
    return render(request,'home_page/search.html',context)


def logouts(request):
    logout(request)
    return HttpResponseRedirect(reverse('login_app:index'))