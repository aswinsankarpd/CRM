# Generated by Django 4.0 on 2021-12-30 17:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0006_rename_product_products'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Products',
            new_name='Product',
        ),
    ]