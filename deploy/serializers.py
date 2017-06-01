from rest_framework import serializers
from deploy.models import Artifact,Component,Manifest,Update,Device
from django.contrib.auth.models import User

class ArtifactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artifact
        fields = ('target', 'type', 'size', 'checksum', 'uri')

class ComponentSerializer(serializers.ModelSerializer):
    artifacts = ArtifactSerializer(many=True)
    class Meta:
        model = Component
        fields = ('type', 'name', 'version', 'checksum', 'artifacts')

    def create(self, validated_data):
        artifacts_data = validated_data.pop('artifacts')
        component = Component.objects.create(**validated_data)
        for a in artifacts_data:
            Artifact.objects.create(component=component, **a)
        return component

class ManifestSerializer(serializers.ModelSerializer):
    components = ComponentSerializer(many=True)
    class Meta:
        model = Manifest
        fields = ('compatible', 'date', 'components')

    def create(self, validated_data):
        components_data = validated_data.pop('components')
        manifest = Manifest.objects.create(**validated_data)
        for c in components_data:
            artifacts_data = c.pop('artifacts')
            component=Component.objects.create(manifest=manifest, **c)
            for a in artifacts_data:
                Artifact.objects.create(component=component, **a)
        return manifest

class UpdateSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    manifest = ManifestSerializer(many=False)
    class Meta:
        model = Update
        fields = ('signature', 'manifest', 'owner')

    def create(self, validated_data):
        manifest_data = validated_data.pop('manifest')
        update = Update.objects.create(**validated_data)

        manifest = Manifest.objects.create(update=update,**manifest_data)
        for c in components_data:
            artifacts_data = c.pop('artifacts')
            component=Component.objects.create(manifest=manifest, **c)
            for a in artifacts_data:
                Artifact.objects.create(component=component, **a)
        return update


class UserSerializer(serializers.ModelSerializer):
    updates = serializers.PrimaryKeyRelatedField(many=True, queryset=Update.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'updates')


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ('uuid', 'product', 'serial', 'mac', 'cert', 'first_seen', 'last_seen', 'last_ip', 'n_requests')

    def create(self, validated_data):
        d = Device.objects.create(**validated_data)
        return d
