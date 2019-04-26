
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class profile(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(default='description default value')
    #location = models.CharField(max_length=120,default='my location default',blank=True,null=True)
    #job = models.CharField(max_length=120,null=True)

    def __unicode__(self):
        return self.name
