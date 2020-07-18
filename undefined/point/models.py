from django.db import models

# Create your models here.
class Point(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    username = models.CharField(max_length=15)
    point_amount = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'point'