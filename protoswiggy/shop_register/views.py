from django.shortcuts import render
from django.utils import timezone
import os
from django.conf import settings
from django.core.files.storage import default_storage

# Create your views here.
from .models import ShopApplications
import uuid

def handle_files(files,name,id):
    ext = os.path.splitext(files.name)[1]
    file_path = os.path.join(settings.BASE_DIR,"shop_register","static","shop_register","application"+str(id),name+ext.lower())
    file_path = default_storage.save(file_path,files)
    path = str(os.path.join("shop_register","application"+str(id),name+ext.lower()))
    print(path)
    return path

def index(request):
    return render(request,'shop_register/index.html')


def upload(request):
    if request.method == "POST" and request.POST['submit']:
        q = ShopApplications()
        q.shop_name = request.POST['shop_name']
        q.shop_owner_name = request.POST['shop_owner_name']
        q.shop_address = request.POST['shop_address']
        q.license_number = request.POST['license_number']
        q.shope_phone = request.POST['shop_phone']
        q.shop_email = request.POST['shop_email']
        q.shop_gst = request.POST['shop_gst']

        id = str(uuid.uuid1())
        q.shop_license_pdf = handle_files(request.FILES['shop_license_pdf'],"license",id)
        
        q.shop_owner_id_proof = handle_files(request.FILES['shop_owner_id_proof'],"shop_owner_id_proof",id)
        
        q.shop_owner_photo = handle_files(request.FILES['shop_owner_photo'],"shop_owner_photo",id)
        q.application_date = timezone.now()
        q.save()

        context = {
            'info':q
        }
        return render(request,'shop_register/upload.html',context)
    else:
        error_message = "Unauthorized Access"
        context = {
            'error_message':error_message,
        }
        return render(request,'shop_register/upload.html',context)