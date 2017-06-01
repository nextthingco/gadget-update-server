# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from deploy.models import Artifact,Component,Manifest,Update
from deploy.serializers import ArtifactSerializer
from deploy.serializers import ComponentSerializer
from deploy.serializers import ManifestSerializer
from deploy.serializers import UpdateSerializer
from deploy.serializers import UserSerializer

from rest_framework import generics
from rest_framework import permissions

from django.contrib.auth.models import User

class ArtifactList(generics.ListCreateAPIView):
    queryset = Artifact.objects.all()
    serializer_class = ArtifactSerializer

class ArtifactDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Artifact.objects.all()
    serializer_class = ArtifactSerializer

class ComponentList(generics.ListCreateAPIView):
    queryset = Component.objects.all()
    serializer_class = ComponentSerializer

class ComponentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Component.objects.all()
    serializer_class = ComponentSerializer


class ManifestList(generics.ListCreateAPIView):
    queryset = Manifest.objects.all()
    serializer_class = ManifestSerializer

class ManifestDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Manifest.objects.all()
    serializer_class = ManifestSerializer



class UpdateList(generics.ListCreateAPIView):
    queryset = Update.objects.all()
    serializer_class = UpdateSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class UpdateDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Update.objects.all()
    serializer_class = UpdateSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from deploy.models import Device
from deploy.serializers import DeviceSerializer

import django
import logging
logger = logging.getLogger('django')
from django.core.exceptions import ObjectDoesNotExist

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

@csrf_exempt
def latest( request ):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        ip=get_client_ip(request)

        try:
            dev=Device.objects.get(uuid=data['uuid'])
            dev.last_seen = django.utils.timezone.now()
            dev.last_ip   = ip 
            dev.n_requests += 1
            dev.save()
            serializer = DeviceSerializer(dev)
            return JsonResponse(serializer.data)
        except ObjectDoesNotExist :
            # could not retrieve dev, try to create
            data['last_ip']=ip
            serializer = DeviceSerializer(data=data)

            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=201)
            return JsonResponse(serializer.errors, status=400)
        return HttpResponse(status=400)

class DeviceList(generics.ListCreateAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

class DeviceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
