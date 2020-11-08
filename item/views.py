from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView


from .models import item

class ItemListView(ListView):
    model = item
    template_name = 'item_list.html'

class ItemDetailView(DetailView):
    model = item
    template_name= 'post_detail.html'
