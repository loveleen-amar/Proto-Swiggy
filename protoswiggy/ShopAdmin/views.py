from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from shop_register.models import ShopApplications

def index(request):
    q = ShopApplications.objects.order_by('application_date')
    context = {
        'list':q
    }
    return render(request,'ShopAdmin/index.html', context)

def detail(request, shop_id):
    shop = ShopApplications.objects.get(pk=shop_id)
    context = {
        'shop':shop,
    }
    return render(request,'ShopAdmin/detail.html',context)