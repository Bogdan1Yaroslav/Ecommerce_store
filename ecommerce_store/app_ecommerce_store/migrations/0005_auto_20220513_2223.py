# Generated by Django 2.2 on 2022-05-13 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_ecommerce_store', '0004_auto_20220511_1546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_name',
            field=models.CharField(db_index=True, max_length=200, verbose_name='Category name'),
        ),
    ]
