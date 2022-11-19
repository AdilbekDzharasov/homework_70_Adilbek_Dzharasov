from django.urls import reverse
from django.views.generic import UpdateView
from webapp.models import Project
from webapp.forms import ProjectForm
from webapp.projects_views.group_permission import GroupPermission


class ProjectUpdateView(GroupPermission, UpdateView):
    model = Project
    form_class = ProjectForm
    template_name = 'projects/update_project.html'
    groups = ['Manager']

    def get_success_url(self):
        return reverse('project_detail', kwargs={'pk': self.object.pk})

