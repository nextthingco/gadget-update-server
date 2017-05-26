from rest_framework import serializers
from deploy.models import Artifact
from deploy.models import Manifest

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

