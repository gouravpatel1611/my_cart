# Generated by Django 3.2.5 on 2021-10-03 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_alter_product_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='model',
            field=models.CharField(default='', max_length=50),
        ),
    ]