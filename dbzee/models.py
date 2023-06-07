from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
STATUS = (
        ('regular', 'regular'),
        ('subscriber', 'subscriber'),
        ('moderator', 'moderator'),
    )




class CustomUser(AbstractUser):

    email = models.EmailField(unique=True)
    status = models.CharField(max_length=100, choices=STATUS, default='regular')
    description = models.TextField("Description", max_length=600, default='', blank=True)
    REQUIRED_FIELDS = []
    
class Meta:  
     db_table = 'auth_AbstractUser'


def __str__(self):
    return self.username
# Create your models here.
