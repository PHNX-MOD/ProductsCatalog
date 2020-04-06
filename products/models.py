from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey(Category, related_name='Category', blank=True, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('product_detail', args=(self.id,))

    def __str__(self):
        return self.name