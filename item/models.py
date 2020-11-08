from django.db import models



class item(models.Model):
    item_name = models.CharField(max_length = 100)
    description = models.TextField(max_length = 500)
    price = models.CharField(max_length = 5)
    def __str__(self):
        return self.item_name
    def get_absolute_url(self):
        return reverse('list_view', args = [str(self.id)])
