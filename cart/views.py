from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
# Create your views here.
from .models import Cart


class CartView(ListView):
    model = Cart
    template_name = 'cart_list.html'
