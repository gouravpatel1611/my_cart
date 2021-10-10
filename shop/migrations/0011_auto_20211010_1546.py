# Generated by Django 3.2.5 on 2021-10-10 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_rename_zip_code_orders_pin_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='address',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='name',
        ),
        migrations.AddField(
            model_name='orders',
            name='address1',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='orders',
            name='address2',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='orders',
            name='address_for_next_time',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='orders',
            name='first_name',
            field=models.CharField(default='', max_length=90),
        ),
        migrations.AddField(
            model_name='orders',
            name='last_name',
            field=models.CharField(default='', max_length=90),
        ),
    ]
