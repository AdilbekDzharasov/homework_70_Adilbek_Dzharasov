from django.shortcuts import render, get_object_or_404
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

    def put(self, request, *args, pk, **kwargs):
        task = get_object_or_404(Task, pk=pk)
        serializer = TaskDetailSerializer(data=request.data, instance=task)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, *args, pk, **kwargs):
        task = get_object_or_404(Task, pk=pk)
        task.delete()
        return Response({
            "message": f"Задача {pk} удалена."
        }, status=204)


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

    def put(self, request, *args, pk, **kwargs):
        project = get_object_or_404(Project, pk=pk)
        serializer = ProjectDetailSerializer(data=request.data, instance=project)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, *args, pk, **kwargs):
        project = get_object_or_404(Project, pk=pk)
        project.delete()
        return Response({
            "message": f"Проект {pk} удален."
        }, status=204)

