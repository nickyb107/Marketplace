from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, DetailView
# Create your views here.
from .models import item
class ItemDetailView(DetailView):
    model = item
