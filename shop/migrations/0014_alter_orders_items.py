# Generated by Django 3.2.5 on 2021-10-11 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0013_orders_total_rs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='items',
            field=models.JSONField(default='', max_length=300),
        ),
    ]
