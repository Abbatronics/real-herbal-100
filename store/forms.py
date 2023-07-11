from django import forms

from .models import Item, Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('first_name', 'last_name', 'address', 'zipcode', 'city', )


class ItemForm(forms.ModelForm):
    class Meta:
       model = Item
       fields = ('category', 'title', 'meta_description', 'price', 'discount_price', 'image', )
       
