from django.db import models
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
    ('V', 'Viagra '),
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


