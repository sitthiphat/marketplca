# Generated by Django 3.0.4 on 2020-04-07 16:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0012_order_orderitem_payment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Payment',
        ),
    ]
