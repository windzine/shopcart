# Generated by Django 3.1.2 on 2020-11-07 07:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20201106_0543'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='product_price',
        ),
    ]
