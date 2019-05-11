from django.db import models
from shop_register.models import Shop
# Create your models here.

class Categories(models.Model):
    category_name = models.CharField(max_length = 50,blank=True)
    def __str__(self):
        return self.category_name

class Units(models.Model):
    units = models.CharField(max_length =50)
    def __str__(self):
      return self.units  

class Product(models.Model):
    product_name = models.CharField(max_length=255,blank = True)
    # category = models.ForeignKey(Categories,on_delete=models.CASCADE,blank = True)
    shop_name = models.ForeignKey(Shop, on_delete=models.CASCADE,blank = True)
    # product_photo = models.FileField(upload_to='product_images', blank = True)
    # quantity = models.IntegerField(max_length=20,blank = True)
    # units = models.ForeignKey(Units, on_delete=models.CASCADE,blank = True)
    rate = models.IntegerField(blank=True)
    product_date = models.DateField('Date Field')
    product_approved = models.CharField(max_length=50)
