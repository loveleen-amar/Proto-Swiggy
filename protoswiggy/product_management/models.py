from django.db import models
from shopadmin.models import Product, Units, Categories
# Create your models here.
from customer_register.models import UserProfile

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    customer = models.ForeignKey(UserProfile, on_delete = models.CASCADE)
    quantity = models.CharField(max_length = 50)
    order_time = models.DateTimeField('Order Time')
    total_cost = models.CharField(max_length = 50)
    order_status = models.CharField(max_length = 50)

    def __str__(self):
        return self.product.product_name

