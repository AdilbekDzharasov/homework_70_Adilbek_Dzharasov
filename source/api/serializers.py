from rest_framework import serializers
from webapp.models import Task


class TaskDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'summary', 'description', 'status', 'type', 'project', 'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at')

