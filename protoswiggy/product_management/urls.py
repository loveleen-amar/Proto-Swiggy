from django.urls import path

from . import views
app_name = 'product_management'
urlpatterns = [
    path('<int:product_id>',views.index,name="index"),
    path('<int:product_id>/order',views.product_order,name="order")
]
