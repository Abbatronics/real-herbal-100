# Generated by Django 3.2.18 on 2023-06-20 19:17

from django.db import migrations, models
import store.models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20230619_2217'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, default='default/no_image.jpg', max_length=255, null=True, upload_to=store.models.Category.image_upload_to),
        ),
    ]
