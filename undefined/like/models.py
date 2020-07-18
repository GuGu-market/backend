from django.db import models

# Create your models here.
class Like(models.Model):
    user_id = models.IntegerField()
    user_name = models.CharField(max_length=15)
    article_id = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'like'