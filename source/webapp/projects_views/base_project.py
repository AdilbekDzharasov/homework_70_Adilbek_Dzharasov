from django.views.generic import ListView
from webapp.models.projects import Project


class HomeProjectView(ListView):
    template_name = 'projects/home_project.html'
    context_object_name = 'projects'
    model = Project

