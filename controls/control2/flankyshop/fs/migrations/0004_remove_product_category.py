# Generated by Django 3.1.5 on 2021-02-08 09:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fs', '0003_product_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
    ]
