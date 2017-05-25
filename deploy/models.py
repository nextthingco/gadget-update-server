# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# "target":   "/data/levels/",
# "type":     "tar",
# "size":     221030201,
# "checksum": "sha256-hash of the data",
# "uri":      "https://update-artifacts.sparkle.co:8079/levels.tar.xz"

class Artifact(models.Model):
    target   = models.CharField(max_length=100)
    type     = models.CharField(max_length=100)
    size     = models.IntegerField()
    checksum = models.CharField(max_length=64,primary_key=True)
    uri      = models.CharField(max_length=256)

    class Meta:
        ordering = ('uri',)
