# Generated by Django 3.2.18 on 2023-06-20 21:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_category_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='image',
        ),
    ]