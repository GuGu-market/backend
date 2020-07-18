from django.db import models

class Signup(models.Model):
    pass
    class Meta:
        def __str__(self):
            return "%s" % (self.ldap)
        def __unicode__(self):
            return u'%s' % (self.ldap)