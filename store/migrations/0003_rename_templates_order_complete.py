# Generated by Django 4.1.7 on 2023-09-23 07:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_customer_order_shippingaddress_orderitem'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='templates',
            new_name='Complete',
        ),
    ]
