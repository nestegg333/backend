from __future__ import unicode_literals

from django.db import models

class Pet(models.Model):
        name = models.CharField(max_length=255)
        created = models.DateTimeField('auto_now_add=True')
        active = models.BooleanField()

