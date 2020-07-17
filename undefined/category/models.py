from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=15)
    category_image = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'cartegory'