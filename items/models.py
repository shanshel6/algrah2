from django.db import models

class Item(models.Model):
    title = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    image = image = models.ImageField(upload_to='images/')
    desc = models.TextField()