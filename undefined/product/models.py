from django.db import models

# Create your models here.
class Product(models.Model):
    category = models.CharField(max_length=30)
    product_name = models.CharField(max_length=15)
    quantity = models.IntegerField()
    price = models.IntegerField()
    product_image = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'product'