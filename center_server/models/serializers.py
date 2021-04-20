from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import File

class FileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = File
        fields = ['version', 'file', 'timestamp']