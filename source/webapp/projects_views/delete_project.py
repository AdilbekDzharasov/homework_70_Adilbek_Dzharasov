from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from webapp.models.projects import Project
from django.views.generic import DeleteView
from webapp.projects_views.group_permission import GroupPermission


class ProjectDeleteView(GroupPermission, LoginRequiredMixin, DeleteView):
    template_name = 'projects/delete_projects.html'
    model = Project
    context_object_name = 'project'
    success_url = reverse_lazy('project_home')
    groups = ['Manager']

