from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Shop(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    
    shop_name = models.CharField(max_length = 200,blank=True)
    shop_owner_name = models.CharField(max_length=200,blank=True)
    shop_address = models.TextField()
    license_number = models.CharField(max_length=200,blank=True)
    shope_phone = models.CharField(max_length=200,blank=True)
    shop_gst = models.CharField(max_length=200,blank=True)
    application_date = models.DateTimeField('Application Date')
    shop_license_pdf = models.FileField(upload_to='docs',blank=True)
    shop_owner_id_proof = models.FileField(upload_to='docs',blank=True)
    shop_owner_photo = models.FileField(upload_to='docs',blank=True)
    shop_approved = models.CharField(max_length =50,blank=True)
    role = models.CharField(max_length=10,blank=True)

    def __str__(self):
        return self.shop_name
