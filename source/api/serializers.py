from rest_framework import serializers
from webapp.models import Task
from webapp.models import Project


class TaskDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'summary', 'description', 'status', 'type', 'project', 'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at')


class ProjectDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'title', 'description', 'is_deleted', 'beginning_date', 'expiration_date', 'created_at', 'deleted_at', 'user', 'is_deleted_user')
        read_only_fields = ('id', 'created_at', 'deleted_at')

