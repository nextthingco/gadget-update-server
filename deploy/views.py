# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from deploy.models import Artifact,Manifest,Update
from deploy.serializers import ArtifactSerializer
from deploy.serializers import ManifestSerializer
from deploy.serializers import UpdateSerializer

from rest_framework import generics


class ArtifactList(generics.ListCreateAPIView):
    queryset = Artifact.objects.all()
    serializer_class = ArtifactSerializer

class ArtifactDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Artifact.objects.all()
    serializer_class = ArtifactSerializer


class ManifestList(generics.ListCreateAPIView):
    queryset = Manifest.objects.all()
    serializer_class = ManifestSerializer

class ManifestDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Manifest.objects.all()
    serializer_class = ManifestSerializer

class UpdateList(generics.ListCreateAPIView):
    queryset = Update.objects.all()
    serializer_class = UpdateSerializer

class UpdateDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Update.objects.all()
    serializer_class = UpdateSerializer
