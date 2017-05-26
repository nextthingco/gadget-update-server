# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Update(models.Model):
    signature   = models.CharField(max_length=1024)

class Manifest(models.Model):
    name        = models.CharField(max_length=100)
    version     = models.CharField(max_length=30)
    date        = models.DateTimeField(auto_now_add=True)
    description = models.TextField(default="")
    compatible  = models.CharField(max_length=30)
    update      = models.OneToOneField(Update, related_name='manifest')

class Artifact(models.Model):
    target   = models.CharField(max_length=100)
    type     = models.CharField(max_length=100)
    size     = models.IntegerField()
    checksum = models.CharField(max_length=64)
    uri      = models.CharField(max_length=256)
    manifest = models.ForeignKey(Manifest, related_name='artifacts')

    class Meta:
        ordering = ('uri',)


