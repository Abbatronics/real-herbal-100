# Generated by Django 3.2.18 on 2023-05-31 07:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_category'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
    ]