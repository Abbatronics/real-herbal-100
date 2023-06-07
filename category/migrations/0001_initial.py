# Generated by Django 3.2.18 on 2023-05-31 07:15

import category.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=150)),
                ('item_name', models.CharField(max_length=150)),
                ('image', models.ImageField(blank=True, null=True, upload_to=category.models.get_file_path)),
                ('description', models.TextField(max_length=500)),
                ('status', models.BooleanField(default=False, help_text='0=default, 1=Hidden')),
                ('meta_title', models.TextField(max_length=150)),
                ('meta_keyword', models.TextField(max_length=150)),
                ('meta_description', models.TextField(max_length=150)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
