from django.urls import reverse
from django.views.generic import DetailView, ListView
# Create your views here.
from .models import Cart, OrderItem
from django.shortcuts import render, redirect, get_object_or_404
from users.models import CustomUser
from item.models import item


class CartView(ListView):
    model = Cart
    template_name = 'cart_list.html'

def add_to_cart(request, **kwargs):
    # get the user profile
    user_profile = get_object_or_404(CustomUser, username=request.user)

    product = item.objects.filter(id=kwargs.get('item_id', "1")).first()

    # create orderItem of the selected product
    order_item, status = OrderItem.objects.get_or_create(item=item)
    user_order.items.add(order_item)
def delete_from_cart(request, item_id):
    item_to_delete = OrderItem.objects.filter(pk=item_id)
    if item_to_delete.exists():
        item_to_delete[0].delete()

    return redirect(reverse('cart:cart_view'))
