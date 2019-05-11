from django.urls import path

from . import views

app_name = 'customerprofile'
urlpatterns = [
    path('',views.index,name='index'),
    path('<int:order_id>/cancel',views.ordercancel,name='ordercancel')
]