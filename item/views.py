from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView

from .models import item, Review

class ItemListView(ListView):
    model = item
    template_name = 'item_list.html'

class ItemDetailView(DetailView):
    model = item
    template_name= 'post_detail.html'

class ReviewCreateView(ListView):
    model = Review
    template_name = 'review.html'
    fields = ('review', 'body', 'author',)
