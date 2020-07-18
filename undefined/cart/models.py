from django.db import models

# Create your models here.
class Cart(models.Model):
    user_id = models.IntegerField()
    user_name = models.CharField(max_length=15)
    category = models.CharField(max_length=15)
    product_id = models.IntegerField()
    product_name = models.CharField(max_length=15)
    quantity = models.IntegerField()
    price = models.IntegerField()
    product_image = models.CharField(max_length=500)
    created_at = models.DateTimeField(format="%Y-%m-%d",input_formats=['%Y-%m-%d',])
    updated_at = models.DateTimeField(format="%Y-%m-%d",input_formats=['%Y-%m-%d',])

    class Meta:
        db_table = 'cart'