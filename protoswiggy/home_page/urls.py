from django.urls import path, include
from home_page import views
app_name = 'home'

urlpatterns = [
    path('',views.home_view, name='index'),
    path('logout',views.logouts,name='logout'),
    path('search',views.search,name='search'),
]
