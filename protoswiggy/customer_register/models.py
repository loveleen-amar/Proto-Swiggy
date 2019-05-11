from django.db import models

from django.contrib.auth.models import User
 
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    customer_name = models.CharField(max_length = 255,blank=True)
    customer_address = models.TextField(default='',blank=True)
    customer_phone = models.CharField(max_length=15,blank=True)
    customer_photo =  models.FileField(upload_to='pictures',blank=True)
    role = models.CharField(max_length=25,blank=True)

    def __str__(self):
        return self.customer_name
