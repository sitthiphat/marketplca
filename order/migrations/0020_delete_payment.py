# Generated by Django 3.0.4 on 2020-04-16 03:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0019_payment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Payment',
        ),
    ]
