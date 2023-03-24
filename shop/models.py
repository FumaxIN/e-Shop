from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.TextField()
    category = models.TextField()
    brandName = models.TextField()
    deleted = models.BooleanField(default=False)
    image = models.ImageField(upload_to='item_cover', blank=True, null=True)
