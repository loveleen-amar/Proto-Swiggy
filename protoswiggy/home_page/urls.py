from django.urls import path, include
from home_page import views
app_name = 'home'
urlpatterns = [
    path('',views.home_view, name='index'),
]