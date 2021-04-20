from rest_framework import serializers
from .models import Task, DLModel

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task,
        fields = '__all__'

class FileExampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = DLModel
        fields = '__all__'