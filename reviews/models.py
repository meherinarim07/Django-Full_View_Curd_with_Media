from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from products.models import Product
# Create your models here.
class Review(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    review_name=models.CharField(max_length=120)
    rating=models.DecimalField(max_digits=2,decimal_places=1,default=5,validators=[MinValueValidator(1),MaxValueValidator(5)],)
    comment=models.TextField(max_length=500)

    def __str__(self):
        return f"{self.review_name}-{self.product.title}"