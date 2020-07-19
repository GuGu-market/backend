from django.db import models

# Create your models here.
class Animal(models.Model):
    user_id = models.IntegerField()
    username = models.CharField(max_length=15, blank=True)
    animal_id = models.IntegerField()
    image = models.CharField(max_length=500, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'animal'
