from django.urls import path

from item.views import ItemDetailView, ItemListView, ReviewCreateView
from cart.views import CartView
urlpatterns = [
    path('',ItemListView.as_view(), name = 'list_view'),
    path('<int:pk>/',ItemDetailView.as_view(), name = 'detail_view'),
    path('cart/', CartView.as_view(), name = 'cart_view'),
    path('new/', ReviewCreateView.as_view(), name = 'review_view'),


]
