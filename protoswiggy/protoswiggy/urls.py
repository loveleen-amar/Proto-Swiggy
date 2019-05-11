"""protoswiggy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import settings
urlpatterns = [
    path('admin/', admin.site.urls,name='admins'),
    path('',include('home_page.urls')),
    path('shopregister/',include('shop_register.urls')),
    path('customerregister/',include('customer_register.urls')),
    path('login/',include('login_app.urls')),
    path('shopadmin/',include('shopadmin.urls')),
    path('customer/',include('customer_profile.urls')),
    path('shop/',include('shop_profile.urls')),
    path('product/',include('product_management.urls')),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
