# Generated by Django 3.2.5 on 2021-08-25 22:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='product_price',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='product_size',
        ),
    ]