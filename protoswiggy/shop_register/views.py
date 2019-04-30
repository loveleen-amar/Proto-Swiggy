from django.shortcuts import render
from django.utils import timezone
# Create your views here.
from .models import ShopApplications
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
        q.shop_license_pdf = request.FILES['shop_license_pdf']
        q.shop_owner_id_proof = request.FILES['shop_owner_id_proof']
        q.shop_owner_photo = request.FILES['shop_owner_photo']
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