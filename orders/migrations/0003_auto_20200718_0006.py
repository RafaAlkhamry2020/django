# Generated by Django 3.0.7 on 2020-07-18 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_image'),
        ('orders', '0002_auto_20200717_1934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='items',
            field=models.ManyToManyField(to='products.Product'),
        ),
    ]
