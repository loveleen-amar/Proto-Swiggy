from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse,HttpResponseRedirect
from customer_register.models import UserProfile
from shop_register.models import Shop
from .models import Categories, Units,Product
# Create your views here.

#views for categories and units
@login_required
def index(request):
    return render(request,'shopadmin/index.html')

@login_required
def categories(request):
    u = Categories.objects.order_by('id')
    units = Units.objects.order_by('id')
    context = {
        'categories':u,
        'units':units,
    }
    return render(request,'shopadmin/category_list.html',context)

@login_required
def add_categories(request):
    if request.method == "POST" and request.POST['submit']:
        c = Categories()
        c.category_name = request.POST['category_name']
        c.save()
        return HttpResponseRedirect(reverse('shopadmin:categories'))

@login_required
def delete_categories(request):
    if request.method == "GET" and request.GET['delete']:
        c = Categories.objects.get(id = request.GET['delete'])
        c.delete()
        return HttpResponseRedirect(reverse('shopadmin:categories'))

@login_required
def add_units(request):
    if request.method == "POST" and request.POST['submit']:
        c = Units()
        c.units = request.POST['unit_name']
        c.save()
        return HttpResponseRedirect(reverse('shopadmin:categories'))

@login_required
def delete_units(request):
    if request.method == "GET" and request.GET['delete']:
        c = Units.objects.get(id = request.GET['delete'])
        c.delete()
        return HttpResponseRedirect(reverse('shopadmin:categories'))

#End Views for categories and units


#views for Shop Applications
@login_required
def shopApplications(request):
        shops = Shop.objects.filter(shop_approved="NOT APPROVED").order_by('-application_date')

        context = {
                'shops':shops
        }
        return render(request,'shopadmin/shop_applications.html',context)

@login_required
def shopApplicationsDetails(request,shop_id):
        user = User.objects.get(id=shop_id)
        shop = Shop.objects.get(user=user)
        context = {
                'info':shop
        }
        return render(request,'shopadmin/shop_application_details.html',context)

@login_required
def shopApplicationsApprove(request,shop_id):
        user = User.objects.get(id=shop_id)
        shop = Shop.objects.get(user=user)
        shop.shop_approved = "APPROVED"
        shop.save()
        return HttpResponseRedirect(reverse('shopadmin:shopApplicationsdetails',args=[shop_id]))


@login_required
def shopApplicationsDelete(request,shop_id):
        user = User.objects.get(id=shop_id)
        user.delete()
        return HttpResponseRedirect(reverse('shopadmin:shopApplications'))
#end of view of Shop Applications


#views for Shop Registered
@login_required
def shopRegistered(request):
        shops = Shop.objects.filter(shop_approved="APPROVED").order_by('-application_date')

        context = {
                'shops':shops
        }
        return render(request,'shopadmin/shop_registered.html',context)

@login_required
def shopRegisteredDetails(request,shop_id):
        user = User.objects.get(id=shop_id)
        shop = Shop.objects.get(user=user)
        context = {
                'info':shop
        }
        return render(request,'shopadmin/shop_registered_details.html',context)

@login_required
def shopRegisteredDelete(request,shop_id):
        user = User.objects.get(id=shop_id)
        user.delete()
        return HttpResponseRedirect(reverse('shopadmin:shopRegistered'))

#end of views for Shop Registered

@login_required 
def productsall(request):
        products = Product.objects.order_by('id')
        context = {
                'products':products
        }
        return render(request,'shopadmin/shop_all_products.html',context)

@login_required 
def productsupdate(request):
        if request.method == 'POST' and request.POST['submit']=="APPROVE":
                P = Product.objects.get(id=request.POST['product_id'])
                P.product_approved = "APPROVED"
                P.save()
                return HttpResponseRedirect(reverse('shopadmin:allproducts'))

        if request.method == 'POST' and request.POST['submit']=="DELETE":
                P = Product.objects.get(id=request.POST['product_id'])
                P.delete()
                return HttpResponseRedirect(reverse('shopadmin:allproducts'))