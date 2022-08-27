# Generated by Django 2.2 on 2022-05-08 19:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_ecommerce_store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(db_index=True, max_length=200, verbose_name='Product name')),
                ('category_slug', models.SlugField(max_length=200, unique=True, verbose_name='Slug')),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'ordering': ('category_name',),
            },
        ),
        migrations.RemoveField(
            model_name='image',
            name='post_id',
        ),
        migrations.CreateModel(
            name='ShoppingCart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchase_date', models.DateField(auto_now_add=True, verbose_name='Purchase date')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'shopping cart',
                'verbose_name_plural': 'shopping carts',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_code', models.CharField(max_length=10, verbose_name='Product code')),
                ('product_slug', models.SlugField(max_length=200, verbose_name='Slug')),
                ('product_name', models.CharField(db_index=True, max_length=2000, verbose_name='Product name')),
                ('product_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Product price in $')),
                ('product_description', models.TextField(blank=True, verbose_name='Product description')),
                ('product_available', models.BooleanField(default=True)),
                ('product_creation_date', models.DateField(auto_now_add=True, verbose_name='Product creation date')),
                ('updated', models.DateField(auto_now=True, verbose_name='Updated')),
                ('images', models.FileField(upload_to='files/', verbose_name='Path')),
                ('product_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app_ecommerce_store.Category', verbose_name='Category name')),
                ('product_seller', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Product seller')),
            ],
            options={
                'verbose_name': 'product',
                'verbose_name_plural': 'products',
                'ordering': ('product_name',),
                'index_together': {('id', 'product_slug')},
            },
        ),
        migrations.AddField(
            model_name='image',
            name='product_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app_ecommerce_store.Product', verbose_name='Product name'),
        ),
    ]