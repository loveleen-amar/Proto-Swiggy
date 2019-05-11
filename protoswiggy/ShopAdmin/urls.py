from django.urls import path

from . import views
app_name = 'shopadmin'
urlpatterns = [
    path('',views.index,name='index'),
    path('category',views.categories,name='categories'),
    path('category/add_c',views.add_categories,name='add_categories'),
    path('category/delete_c',views.delete_categories,name='delete_categories'),
    path('category/add_u',views.add_units,name='add_units'),
    path('category/delete_u',views.delete_units,name='delete_units'),
    path('shopApplications',views.shopApplications,name="shopApplications"),
    path('shopApplications/<int:shop_id>',views.shopApplicationsDetails,name="shopApplicationsdetails"),
    path('shopApplications/<int:shop_id>/approve',views.shopApplicationsApprove,name="shopApplicationsApprove"),
    path('shopApplications/<int:shop_id>/delete',views.shopApplicationsDelete,name="shopApplicationsDelete"),
    path('shopRegistered',views.shopRegistered,name="shopRegistered"),
    path('shopRegistered/<int:shop_id>',views.shopRegisteredDetails,name="shopRegistereddetails"),
    path('shopRegistered/<int:shop_id>/delete',views.shopRegisteredDelete,name="shopRegisteredDelete"),
    path('allproducts',views.productsall,name="allproducts"),
    path('allproducts/update',views.productsupdate,name="productsupdate"),
]
