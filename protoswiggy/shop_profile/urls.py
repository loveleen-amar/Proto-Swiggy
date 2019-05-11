from django.urls import path

from . import views

app_name = 'shop_profile'
urlpatterns = [
    path('',views.index,name='index'),
    path('productupdate',views.productupdate,name='productupdate'),
    path('orderupdate/<int:order_id>',views.orderupdate, name='orderupdate')
]
