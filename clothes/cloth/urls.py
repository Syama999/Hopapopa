from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from cloth.views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('add_product', AddProduct.as_view(), name='add_product'),
    path('brand_collection', BrandCollection.as_view(), name='brand_collection'),
    path('new_products', NewProducts.as_view(), name='new_products'),
    path('favourite', Favourite.as_view(), name='favourite'),
    path('sale', Sale.as_view(), name='sale'),

]