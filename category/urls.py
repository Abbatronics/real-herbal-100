from django.urls import path


app_name = 'category'

urlpatterns =[
    path('collections', views.collections, name="collections"),
    path('collections/<str:slug>', views.collectionsveiw, name="collectionsveiw"),

]
 