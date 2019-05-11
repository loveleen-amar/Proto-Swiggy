from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.urls import reverse
from .models import UserProfile
# Create your views here.
def index(request):
    return render(request, 'customer_register/index.html')

def validate(request):
    if request.method == 'POST':
        try:
            u1 = User.objects.create(username=request.POST['customer_username'])
            u1.set_password(request.POST['customer_password'])
            u1.email = request.POST['customer_email']
            c = UserProfile()
            c.customer_name = request.POST['customer_name']
            c.customer_address = request.POST['customer_address']
            c.customer_phone = request.POST['customer_phone']
            c.customer_name = request.POST['customer_name']
            c.customer_photo = request.FILES['customer_photo']
            c.role = 'customer'
            c.user = u1
            u1.save()
            c.save()
            return render(request,'customer_register/upload.html')
        except:
            context = {
                'error_message' : "Username Already Exists",
            }
            return render(request,'customer_register/index.html',context)
    return redirect('customerregister:index')