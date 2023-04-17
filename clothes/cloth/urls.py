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
    path('shoppingcart', ShoppingCart.as_view(), name='shoppingcart'),
    path('profile', Profile.as_view(), name='profile'),
    path('brand_profile', BrandProfile.as_view(), name='brand_profile'),
    path('collections', Collections.as_view(), name='collections'),
    path('delivery_adress', DeliveryAdress.as_view(), name='delivery_adress'),
    path('new_look', NewLook.as_view(), name='new_look'),
    path('product_card', ProductCard.as_view(), name='product_card'),
    path('search', Search.as_view(), name='search'),
    path('top_products', TopProducts.as_view(), name='top_products'),
    path('view_brand_profile', ViewBrandProfile.as_view(), name='view_brand_profile'),

]