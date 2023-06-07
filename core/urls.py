from django.urls import path
from django.contrib.auth import views as auth_views 
from django.conf import settings
from django.conf.urls.static import static

from django.contrib.staticfiles.urls import staticfiles_urlpatterns



from .views import (
    remove_from_cart,
    reduce_quantity_item,
    add_to_cart,
    ProductView,
    HomeView,
    OrderSummaryView,
    CheckoutView,
    PaymentView,
     
       
)

app_name = 'core'

urlpatterns = [

    
    
    
    path('', HomeView.as_view(), name='home'),
    path('product/<pk>/', ProductView.as_view(), name='product'),
    path('add-to-cart/<pk>/', add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<pk>/', remove_from_cart, name='remove-from-cart'),
    path('order-summary', OrderSummaryView.as_view(), 
        name='order-summary'),
    path('reduce-quantity-item/<pk>/', reduce_quantity_item,
        name='reduce-quantity-item'),
    path('checkout', CheckoutView.as_view(), name='checkout'),
    path('payment/<payment_option>/', PaymentView.as_view(), name='payment')
    
   

]
urlpatterns += staticfiles_urlpatterns()
if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT ) 

