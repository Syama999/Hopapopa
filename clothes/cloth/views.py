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