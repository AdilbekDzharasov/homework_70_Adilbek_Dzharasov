from django.urls import path
from api.views import TaskDetailView

app_name = "api"

urlpatterns = [
   path('tasks/detail/<int:pk>/', TaskDetailView.as_view())
]

