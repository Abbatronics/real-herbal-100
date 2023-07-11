from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify
import os
import datetime
import secrets


from django.core.files import File

from io import BytesIO
from PIL import Image





class Category(models.Model):
    def image_upload_to(self, instance=None):
        if instance:
            return os.path.join("Item", instance)
        return None
 
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    
    class Meta:
        verbose_name_plural =  'Categories'

    def __str__(self):
        return self.title


class Item(models.Model):
    def image_upload_to(self, instance=None):
        if instance:
            return os.path.join("Item", instance)
        return None

    DRAFT = 'draft '
    WAITING_APPROVAL = 'waitingapproval '
    ACTIVE = 'active '
    DELETED = 'deleted'

    STATUS_CHOICES = (
        (DRAFT, 'draft'),
        (WAITING_APPROVAL, 'waitingapproval'),
        (ACTIVE, 'active'),
        (DELETED, 'deleted'),
    )
 
    user = models.ForeignKey(User, related_name='products', on_delete=models.CASCADE, default=True)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    meta_description = models.TextField(blank=True)
    discount_price = models.FloatField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    image = models.ImageField(default='default/no_image.jpg', upload_to=image_upload_to ,max_length=255, blank=True, null=True)
    thumbnail = models.ImageField(upload_to='uploads/item_images/thumbnail/', blank=True, null=True) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default=ACTIVE)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.title

    def get_display_price(self):
        return self.price / 100
        return self.discount_price / 100


    def get_thumbnail(self):
        if self.thumbnail:
            return self.thumbnail.url
        
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()
                
                return self.thumbnail.url
            else:
                return 'https://via.placeholder.com/240x240x.jpg'




    def make_thumbnail(self, image, size=(3000, 300)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)
        thumbnail = File(thumb_io, name=image.name)

        return thumbnail

class Order(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    paid_amount = models.IntegerField(blank=True, null=True)
    is_paid = models.BooleanField(default=False)
    payment_intent = models.CharField(max_length=255)
    created_by = models.ForeignKey(User, related_name='orders', on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Item, related_name='items', on_delete=models.CASCADE)
    price = models.IntegerField()
    quantity = models.IntegerField(default=1)

   