# Generated by Django 5.0.2 on 2024-02-26 12:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_product'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Product',
            new_name='Products',
        ),
    ]