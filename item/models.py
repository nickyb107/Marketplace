from django.db import models

# Create your models here.
class item(models.Model):
    item_name = models.CharField(max_length = 100)
    description = models.TextField(max_length = 500)
    price = models.CharField(max_length = 5)
