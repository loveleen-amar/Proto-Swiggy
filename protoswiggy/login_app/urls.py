from django.urls import path

from . import views

app_name = "login_app"

urlpatterns = [
    path('',views.index, name = 'index'),
    path('login',views.login_user,name="login_user"),
    path('login/user',views.main_logged_in,name="logged_in"),
]