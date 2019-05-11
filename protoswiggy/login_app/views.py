from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse,HttpResponseRedirect
from customer_register.models import UserProfile
from shop_register.models import Shop

# Create your views here.
def index(request):
    if request.user is not None:
        if request.user.is_active:
            return HttpResponseRedirect(reverse('login_app:logged_in'))

    return render(request, 'login_app/index.html')

def login_user(request):
    logout(request)
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('login_app:logged_in'))
        context = {
            'error_message':"Username or Password Doesn't exist"
        }
        return render(request,'login_app/index.html',context)

@login_required     
def main_logged_in(request):
    user = request.user
    try:
        u = UserProfile.objects.get(user = user)
        if u is not None:
            return HttpResponseRedirect(reverse('customerprofile:index'))
    except:
        try:
            u = Shop.objects.get(user = user)
            if u is not None:
                return HttpResponseRedirect(reverse('shop_profile:index'))
        except:
            return HttpResponseRedirect(reverse('shopadmin:index'))

    return HttpResponse("Not Authorized")
    
