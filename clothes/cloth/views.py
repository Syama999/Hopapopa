from django.shortcuts import render
from .models import *
from django.views.generic import TemplateView, ListView, DetailView, CreateView
# Create your views here.
class Home(ListView):
    model = Cloth
    context_object_name = 'clothobj'
    template_name = 'cloth/home.html'
    #return render(request, 'cloth/home.html/')

class AddProduct(ListView):
    model = Cloth
    context_object_name = 'addproduct'
    template_name = 'cloth/add_product.html'

class BrandCollection(ListView):
    model = Cloth
    context_object_name = 'brandcollection'
    template_name = 'cloth/brand_collection.html'

class NewProducts(ListView):
    model = Cloth
    context_object_name = 'newproducts'
    template_name = 'cloth/new_products.html'


class Favourite(ListView):
    model = Cloth
    context_object_name = 'favourite'
    template_name = 'cloth/favourite.html'


class Sale(ListView):
    model = Cloth
    context_object_name = 'sale'
    template_name = 'cloth/sale.html'

class ShoppingCart(ListView):
    model = Cloth
    context_object_name = 'shoppingcart'
    template_name = 'cloth/shoppingcart.html'

class Profile(ListView):
    model = Cloth #надо будет точно исправлять
    context_object_name = 'profile'
    template_name = 'cloth/profile.html'

class BrandProfile(ListView):
    model = Cloth #надо будет точно исправлять
    context_object_name = 'brand_profile'
    template_name = 'cloth/brand_profile.html'

class Collections(ListView):
    model = Cloth #надо будет точно исправлять
    context_object_name = 'collections'
    template_name = 'cloth/collections.html'

class DeliveryAdress(ListView):
    model = Cloth
    context_object_name = 'delivery_adress'
    template_name = 'cloth/delivery_adress.html'

class NewLook(ListView):
    model = Cloth
    context_object_name = 'new_look'
    template_name = 'cloth/new_look.html'


class ProductCard(ListView):
    model = Cloth
    context_object_name = 'product_card'
    template_name = 'cloth/product_card.html'


class Search(DetailView):
    model = Cloth
    context_object_name = 'search'
    template_name = 'cloth/search.html'


class TopProducts(ListView):
    model = Cloth
    context_object_name = 'top_products'
    template_name = 'cloth/top_products.html'


class ViewBrandProfile(ListView):
    model = Cloth
    context_object_name = 'view_brand_profile'
    template_name = 'cloth/view_brand_profile.html'


