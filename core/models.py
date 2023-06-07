from django.conf import settings
from django.db import models
from django.shortcuts import reverse
from django_countries.fields import CountryField

from django.template.defaultfilters import slugify
import os
import datetime



CATEGORY = (
    ('A', 'Aphrodisiac '),
    ('PB', 'Power Booster'),
    ('T', 'Tea'),
    ('HS', 'Herbal Supliments'),
    ('M', 'Medicine' ),
    ('E', 'Essence '),
    ('D', 'Distilate '),
    ('V', 'Viaga '),
    ('TN', 'Tonics '),
    ('S', 'Supplements ')
)

LABEL = (
    ('N', 'New'),
    ('BS', 'Best Seller'),
    ('SO', 'Special offer'),
    ('R', 'Ramadan offer'),
    ('P', 'Promo'),
    ('PQ', 'Premium Quality '),
    ('NA', 'Naural')
) 

class Item(models.Model):
    def image_upload_to(self, instance=None):
        if instance:
            return os.path.join("Item", instance)
        return None

        
    item_name = models.CharField(max_length=100)
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True) 
    label = models.CharField(choices=LABEL, max_length=2)
    description = models.TextField()
    image = models.ImageField(default='default/no_image.jpg', upload_to=image_upload_to ,max_length=255)


    def __str__(self):
        return self.item_name

    def get_absolute_url(self):
        return reverse("core:product", kwargs={
            "pk" : self.pk
        
        })

    def get_add_to_cart_url(self):
        return reverse("core:add-to-cart", kwargs={
            "pk" : self.pk
        })

    def get_remove_from_cart_url(self):
        return reverse("core:remove-from-cart", kwargs={
            "pk" : self.pk
        })

def get_file_path(request, filename):
    original_filename = filename
    nowTime = datetime.datetime.now().strftime('%Y%n%d%H:%M:%S')
    filename = '%s%s' %(nowTime, original_filename)
    return os.path.join('uploads/', filename)



    

class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.item.item_name}"

    def get_total_item_price(self):
        return self.quantity * self.item.price

    def get_discount_item_price(self):
        return self.quantity * self.item.discount_price

    def get_amount_saved(self):
        return self.get_total_item_price() - self.get_discount_item_price()

    def get_final_price(self):
        if self.item.discount_price:
            return self.get_discount_item_price()
        return self.get_total_item_price()
    
    

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)
    checkout_address = models.ForeignKey(
        'CheckoutAddress', on_delete=models.SET_NULL, blank=True, null=True)
    payment = models.ForeignKey(
        'Payment', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.user.username
    
    def get_total_price(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_final_price()
        return total


class CheckoutAddress(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    street_address = models.CharField(max_length=100)
    apartment_address = models.CharField(max_length=100)
    country = CountryField(multiple=False)
    zip = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username
    
class Payment(models.Model):
    stripe_id = models.CharField(max_length=50)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, 
                             on_delete=models.SET_NULL, blank=True, null=True)
    amount = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
    