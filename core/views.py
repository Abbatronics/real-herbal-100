from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, View 
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import reverse
from  django.db import models
from store.models import Item 
from django.contrib.auth.models import User 
from django.utils import timezone
from .form import CheckoutForm
from store.models import Item
#from .models import  (
    #Item,
    #Order,
    #OrderItem,
    #CheckoutAddress,
    #Payment
    
#)



# Create your views here.
class HomeView(ListView):
    model = Item
    template_name = "home.html"
    def home(request):
       product =Item.objects.filter(status=Product.ACTIVE)[0:8]
       context = {'products' :products}
       return render(request, 'products/home.html', context)

#class ProductView(DetailView):
    #model = Item
    #template_name = "product.html"
    

