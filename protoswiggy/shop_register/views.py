from django.shortcuts import render
from django.utils import timezone
import os
from django.conf import settings
from django.core.files.storage import default_storage

# Create your views here.
from .models import Shop
from django.contrib.auth.models import User


def index(request):
    return render(request,'shop_register/index.html')


def upload(request):
    if request.method == "POST" and request.POST['submit']:
        try:
            user = User.objects.create(username = request.POST['shop_username'])
            user.set_password(request.POST['shop_password'])
            user.email = request.POST['shop_email']
            q = Shop()
            q.shop_name = request.POST['shop_name']
            q.shop_owner_name = request.POST['shop_owner_name']
            q.shop_address = request.POST['shop_address']
            q.license_number = request.POST['license_number']
            q.shope_phone = request.POST['shop_phone']
            q.shop_email = request.POST['shop_email']
            q.shop_gst = request.POST['shop_gst']

            q.shop_license_pdf = request.FILES['shop_license_pdf']
            
            q.shop_owner_id_proof = request.FILES['shop_owner_id_proof']
            
            q.shop_owner_photo = request.FILES['shop_owner_photo']
            q.application_date = timezone.now()
            q.role = 'shop'
            q.shop_approved = "NOT APPROVED"
            q.user = user
            user.save()
            q.save()

            context = {
                'info':q,
                'user':user
            }

            return render(request,'shop_register/upload.html',context)
        except:
            error_message = "Unauthorized Access"
            context = {
                'error_message':error_message,
            }
            return render(request,'shop_register/index.html',context)
    else:
        error_message = "Unauthorized Access"
        context = {
            'error_message':error_message,
        }
        return render(request,'shop_register/upload.html',context)