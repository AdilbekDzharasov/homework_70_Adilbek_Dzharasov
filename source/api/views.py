from rest_framework.views import APIView
from api.serializers import TaskDetailSerializer
from rest_framework.response import Response
from webapp.models import Task
from rest_framework import status


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
