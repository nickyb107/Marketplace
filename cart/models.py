from django.db import models


class Cart(models.Model):
    item_name = models.CharField(max_length = 100)
    in_cart = models.BooleanField()
    price = models.CharField(max_length = 5)
    def __str__(self):
        return self.item_name
    def get_absolute_url(self):
        return reverse('cart_view', args = [str(self.id)])
