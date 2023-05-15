from django.db import models

# Create your models here.

class ProductCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    descrption = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='products_images')
    category = models.ForeignKey(to=ProductCategory, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'Продукт: {self.name} / Категория: {self.category.name}'

    