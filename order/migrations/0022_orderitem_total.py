# Generated by Django 3.0.4 on 2020-04-27 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0021_auto_20200427_0818'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='total',
            field=models.FloatField(null=True),
        ),
    ]
