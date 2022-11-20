from rest_framework.views import APIView
from api.serializers import TaskDetailSerializer
from rest_framework.response import Response
from webapp.models import Task
from rest_framework import status
from api.serializers import ProjectDetailSerializer
from webapp.models import Project


class TaskDetailView(APIView):
    def get(self, request, pk):
        try:
            task = Task.objects.get(pk=pk)
            serializer = TaskDetailSerializer(task)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({
                "message": "Задача не найдена."
            }, status=404)


class ProjectDetailView(APIView):
    def get(self, request, pk):
        try:
            project = Project.objects.get(pk=pk)
            serializer = ProjectDetailSerializer(project)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({
                "message": "Проект не найден."
            }, status=404)

