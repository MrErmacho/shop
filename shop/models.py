from django.db import models

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=30)
    img = models.ImageField(upload_to='img/')
    description = models.TextField()
    price = models.PositiveBigIntegerField()
    added_at = models.DateTimeField(auto_now_add=True)
    rating = models.PositiveSmallIntegerField()
    discount = models.PositiveSmallIntegerField(default=0)
    stock = models.PositiveIntegerField()
    manufacturer = models.CharField(max_length=30)

