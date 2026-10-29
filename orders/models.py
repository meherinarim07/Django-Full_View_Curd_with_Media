from django.db import models
from products.models import Product

# Create your models here.
class Order(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    order_time=models.DateTimeField(auto_now_add=True)
    customer_name=models.CharField(max_length=50)
    email=models.EmailField(null=True,blank=True)
    quantity=models.PositiveIntegerField(default=1)
    @property
    def total(self):
        return self.quantity*self.product.price

    def __str__(self):
        return f"{self.customer_name}-{self.product.title}"