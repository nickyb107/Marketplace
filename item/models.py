from django.db import models
from django.contrib.auth import get_user_model



class item(models.Model):
    item_name = models.CharField(max_length = 100)
    description = models.TextField(max_length = 500)
    in_cart = models.BooleanField(default = False)
    price = models.CharField(max_length = 5)
    def __str__(self):
        return self.item_name
    def get_absolute_url(self):
        return reverse('list_view', args = [str(self.id)])

class Review(models.Model):
    review = models.ForeignKey(item , on_delete = models.CASCADE , related_name = 'reviews',)
    body = models.CharField(max_length = 255)
    author = models.ForeignKey(
        get_user_model(),
        on_delete = models.CASCADE,

    )
    def __str__(self):
        return self.body

    def get_absolute_url(self):
        return reverse('detail_view')
