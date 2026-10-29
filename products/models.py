from django.db import models

# Create your models here.
class Product(models.Model):
    title=models.CharField(max_length=50)
    image=models.ImageField(upload_to='products/',blank=True,null=True)
    description=models.TextField(max_length=100)
    price=models.DecimalField(max_digits=8,decimal_places=2)

    def __str__(self):
        return f"{self.title}-({self.price})"