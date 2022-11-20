from django.urls import path
from api.views import TaskDetailView, ProjectDetailView

app_name = "api"

urlpatterns = [
   path('tasks/detail/<int:pk>/', TaskDetailView.as_view()),
   path('projects/detail/<int:pk>/', ProjectDetailView.as_view()),
]

