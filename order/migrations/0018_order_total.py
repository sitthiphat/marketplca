# Generated by Django 3.0.4 on 2020-04-12 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0017_remove_order_nameorder'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total',
            field=models.FloatField(null=True),
        ),
    ]
