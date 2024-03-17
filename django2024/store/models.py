from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=100)
    discription = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f"{self.name}, {self.discription}, ${self.price}"
