from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView
# Create your views here.
def home(request):
    return render(request, 'cloth/home.html/')
#hhh