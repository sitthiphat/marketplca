# Generated by Django 3.0.4 on 2020-04-27 04:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0022_orderitem_total'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='total',
        ),
    ]
