from django.urls import path

from . import views
app_name ='customerregister'
urlpatterns = [
    path('',views.index,name='index'),
    path('validate',views.validate,name='validate')
]