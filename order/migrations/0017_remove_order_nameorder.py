# Generated by Django 3.0.4 on 2020-04-12 09:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0016_order_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='nameorder',
        ),
    ]
