from django.urls import path

from . import views

urlpatterns = [
    path('/ShopAdmin', views.index, name='index'),
]