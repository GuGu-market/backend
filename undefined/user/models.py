from django.db import models

# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=30)
    username = models.CharField(max_length=15, default='')
    image = models.CharField(max_length=500)
    grade = models.IntegerField(default=1)
    activate = models.BooleanField(default=True)
    phone = models.CharField(max_length=13)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'user'

    def get_by_natural_key(self, username):
        return self.get(username=username)