from django.shortcuts import render
from django.conf import settings
from django.contrib import messages
from .models import *


def collections(request):
    category = Category.objects.filter(status=0)
    context = ('category':category)
    return render(request, "collections.html", context)

def collectionsveiw(request, slug):
    if(category.object.filter(slug=slug, status=0)):  
       products = product.objects.filter(category__slug) 
       context = {'products': products}
       return render(request, "products/home.html", context)
    else:
        messages.warning(request, " No such category found ")
        return redirect('collections')
