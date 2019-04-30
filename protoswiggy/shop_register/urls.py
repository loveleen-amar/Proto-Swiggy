from django.urls import path,include

from . import views

app_name = 'shopregister'

urlpatterns= [
    path('',views.index,name="index"),
    path('upload/',views.upload,name='upload')
]

