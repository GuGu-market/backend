from django.db import models

# Create your models here.
class Users(models.Model):
    email = models.CharField(max_length=30)
    user_name = models.CharField(max_length=15)
    password = models.CharField(max_length=30)
    grade = models.IntegerField()
    activate = models.BooleanField()
    phone = models.CharField(max_length=13)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        def __str__(self):
            return "%s" % (self.ldap)
        def __unicode__(self):
            return u'%s' % (self.ldap)