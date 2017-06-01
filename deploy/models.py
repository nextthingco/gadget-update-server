# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Update(models.Model):
    signature = models.CharField(max_length=1024)
    owner     = models.ForeignKey('auth.User', related_name='updates', on_delete=models.CASCADE)

class Manifest(models.Model):
    compatible  = models.CharField(max_length=30)
    date        = models.DateTimeField(auto_now_add=True)
    update      = models.OneToOneField(Update, related_name='manifest')

class Component(models.Model):
    type     = models.CharField(max_length=100)
    name     = models.CharField(max_length=100)
    version  = models.CharField(max_length=100)
    checksum = models.CharField(max_length=64)
    manifest = models.ForeignKey(Manifest, related_name='components')

class Artifact(models.Model):
    target    = models.CharField(max_length=100)
    type      = models.CharField(max_length=100)
    size      = models.IntegerField()
    checksum  = models.CharField(max_length=64)
    uri       = models.CharField(max_length=256)
    component = models.ForeignKey(Component, related_name='components')

class Device(models.Model):
    uuid          = models.UUIDField(primary_key=True)
    product       = models.CharField(max_length=100)
    serial        = models.CharField(max_length=100)
    mac           = models.CharField(max_length=17)
    cert          = models.CharField(max_length=1024)
    first_seen    = models.DateTimeField(auto_now_add=True)
    last_seen     = models.DateTimeField(auto_now_add=True)
    last_ip       = models.CharField(max_length=15)
    n_requests    = models.PositiveIntegerField(default=1)
