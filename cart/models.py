from django.db import models
from django.contrib.auth import get_user_model
from item.models import item
from users.models import CustomUser

class OrderItem(models.Model):
    product = models.OneToOneField(item, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.product.name

class Cart(models.Model):
    user =  models.ForeignKey(CustomUser, null=True, blank=True, on_delete = models.CASCADE)
    items = models.ManyToManyField(OrderItem)

    def get_absolute_url(self):
        return reverse('cart_view', args = [str(self.id)])
    def get_cart_items(self):
        return self.items.all()
    def get_cart_total(self):
        return sum([items.price for item in self.items.all()])
