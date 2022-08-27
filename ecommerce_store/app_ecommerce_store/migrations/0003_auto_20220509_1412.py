# Generated by Django 2.2 on 2022-05-09 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_ecommerce_store', '0002_auto_20220508_2202'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='images',
        ),
        migrations.AddField(
            model_name='product',
            name='product_images',
            field=models.ImageField(blank=True, upload_to='files/products/%Y/%m/%d'),
        ),
    ]