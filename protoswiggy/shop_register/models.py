from django.db import models

# Create your models here.

class ShopApplications(models.Model):
    shop_name = models.CharField(max_length = 200)
    shop_owner_name = models.CharField(max_length=200)
    shop_address = models.TextField()
    license_number = models.CharField(max_length=200)
    shope_phone = models.CharField(max_length=200)
    shop_email = models.EmailField()
    shop_gst = models.CharField(max_length=200)
    application_date = models.DateTimeField('Application Date')
    shop_license_pdf = models.CharField(max_length=1000)
    shop_owner_id_proof = models.CharField(max_length=1000)
    shop_owner_photo = models.CharField(max_length=1000)

    def __str__(self):
        return self.shop_name
