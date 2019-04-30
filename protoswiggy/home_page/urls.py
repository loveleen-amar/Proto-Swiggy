from django.urls import path, include
from home_page import views

urlpatterns = [
    path('',views.home_view),
]