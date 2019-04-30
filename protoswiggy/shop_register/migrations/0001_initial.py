# Generated by Django 2.2 on 2019-04-30 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShopApplications',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shop_name', models.CharField(max_length=200)),
                ('shop_owner_name', models.CharField(max_length=200)),
                ('shop_address', models.TextField()),
                ('license_number', models.CharField(max_length=200)),
                ('shope_phone', models.CharField(max_length=200)),
                ('shop_email', models.EmailField(max_length=254)),
                ('shop_gst', models.CharField(max_length=200)),
                ('application_date', models.DateField(verbose_name='Application Date')),
                ('shop_license_pdf', models.CharField(max_length=1000)),
                ('shop_owner_id_proof', models.CharField(max_length=1000)),
                ('shop_owner_photo', models.CharField(max_length=1000)),
            ],
        ),
    ]
