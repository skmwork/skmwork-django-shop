# Generated by Django 3.1 on 2020-11-28 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_auto_20201128_1410'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='cartitem',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
