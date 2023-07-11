from django.conf import settings
from django.db import models
from django.shortcuts import reverse
from django_countries.fields import CountryField
from django.contrib.auth.models import User
from  django.db import models

from django.template.defaultfilters import slugify
import os
import datetime





LABEL = (
    ('N', 'New'),
    ('BS', 'Best Seller'),
    ('SO', 'Special offer'),
    ('R', 'Ramadan offer'),
    ('P', 'Promo'),
    ('PQ', 'Premium Quality '),
    ('NA', 'Naural')
) 

def get_file_path(request, filename):
    original_filename = filename
    nowTime = datetime.datetime.now().strftime('%Y%m%d%h:%M:%s')
    filename = "%s%s" % (nowTime.original_filename)
    return os.path.join('uploads/', filename)



    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("core:product", kwargs={
            "pk" : self.pk
        
        })


#class Item(models.Model):
    def image_upload_to(self, instance=None):
        if instance:
            return os.path.join("Item", instance)
        return None
 
    #user = models.ForeignKey(User, related_name='products', on_delete=models.CASCADE, default=True)
    #category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    #title = models.CharField(max_length=50)
    #slug = models.SlugField(max_length=50, default=True)
    #price = models.FloatField()
    #discount_price = models.FloatField(blank=True, null=True) 
    #label = models.CharField(choices=LABEL, max_length=2)
    ##image = models.ImageField(default='default/no_image.jpg', upload_to=image_upload_to ,max_length=255)
    


    


    
    

