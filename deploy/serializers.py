from rest_framework import serializers
from deploy.models import Artifact,Manifest,Update

class ArtifactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artifact
        fields = ('target', 'type', 'size', 'checksum', 'uri')

class ManifestSerializer(serializers.ModelSerializer):
    artifacts = ArtifactSerializer(many=True)
    class Meta:
        model = Manifest
        fields = ('name', 'version', 'date', 'description', 'compatible', 'artifacts')

    def create(self, validated_data):
        artifacts_data = validated_data.pop('artifacts')
        manifest = Manifest.objects.create(**validated_data)
        for a in artifacts_data:
            Artifact.objects.create(manifest=manifest, **a)
        return manifest

class UpdateSerializer(serializers.ModelSerializer):
    manifest = ManifestSerializer(many=False)
    class Meta:
        model = Update
        fields = ('signature', 'manifest')

    def create(self, validated_data):
        manifest_data = validated_data.pop('manifest')
        update = Update.objects.create(**validated_data)
        artifacts_data = manifest_data.pop('artifacts')
        manifest = Manifest.objects.create(update=update,**manifest_data)
        for a in artifacts_data:
            Artifact.objects.create(manifest=manifest, **a)

        return update
