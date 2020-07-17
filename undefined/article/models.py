from django.db import models

# Create your models here.
class Article(models.Model):
    user_id = models.IntegerField()
    user_name = models.CharField(max_length=15)
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=50)
    image = models.CharField(max_length=500)
    like_count = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'article'