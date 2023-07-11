from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.utils.text import slugify

from .models import Userprofile 
from store.forms import ItemForm
from store.models import Item, Order, OrderItem



def vendor_detail(request, pk):
    user = User.objects.get(pk=pk)
    products = user.products.filter(status=Item.ACTIVE)

    return render(request, 'userprofile/vendor_detail.html', {
        'user': user,
        'products': products
    })

@login_required
def add_product(request):
    

    if request.method == "POST":
        form = ItemForm(request.POST, request.FILES)

        if form.is_valid():
            title = request.POST.get('title', )
            slug = slugify(title)

            item = form.save(commit=False)
            item.user = (request.user)
            item.slug = slug
            item.save()

            messages.success(request, 'The product was added !')

            return redirect('my_store')
    else:        
        form = ItemForm()


    return render(request, 'userprofile/add_product.html', {
        'title': 'Add product ', 
        'form': form
    })

@login_required
def edit_product(request, pk):
    product = Item.objects.filter(user=request.user).get(pk=pk)

    if request.method == "POST":
        form = ItemForm(request.POST, request.FILES, instance=product)

        if form.is_valid():
           form.save()

           messages.success(request, 'The product was edited !')


           return redirect('my_store')

    else:    
        form = ItemForm(instance=product)

    return render(request, 'userprofile/add_product.html', {
        'title': 'Edit product ',
        'product': product , 
        'form': form
    })

@login_required
def delete_product(request, pk):
    product = Item.objects.filter(user=request.user).get(pk=pk)
    product.status = Product.DELETED
    product.save()
    
    messages.success(request, 'The product was deleted !')

    return redirect( 'my_store')
    

@login_required
def my_store(request):
    products = request.user.products.exclude(status=Item.DELETED)
    order_items = OrderItem.objects.filter(product__user=request.user)

    return render(request, 'userprofile/my_store.html', {
        'products': products,
        'order_items': order_items
    })

@login_required
def my_store_order_detail(request, pk):
    order = get_object_or_404(Order, pk=pk)

    return render(request, 'userprofile/my_store_order_detail.html', {
        'order': order
    })
    
@login_required
def myaccount(request):
    return render(request, 'userprofile/myaccount.html')

def signup(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == "POST":
        form =  UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user, backend='django.contrib.auth.backends.ModelBackend')

            userprofile = Userprofile.objects.create(user=user)

            return redirect('home ')
    else:
        form = UserCreationForm()

    return render(
        request=request,
        template_name = "userprofile/signup.html",
        context={"form": form}
    )
    