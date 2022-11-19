from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.generic import DetailView, CreateView, UpdateView
from webapp.forms import ProjectForm
from webapp.models.projects import Project
from webapp.forms import ProjectAddUserForm
from webapp.projects_views.group_permission import GroupPermission


class ProjectAddView(GroupPermission, LoginRequiredMixin, CreateView):
    template_name = 'projects/add_project.html'
    model = Project
    form_class = ProjectForm
    groups = ['Manager']

    def get_success_url(self):
        return reverse('project_detail', kwargs={'pk': self.object.pk})


class ProjectDetailView(DetailView):
    template_name = "projects/project.html"
    model = Project

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = self.object.tasks.order_by("-created_at")
        return context


class ProjectAddUserView(GroupPermission, PermissionRequiredMixin, UpdateView):
    model = Project
    template_name = 'projects/projects_user_add.html'
    form_class = ProjectAddUserForm
    permission_required = 'webapp.add_task'
    groups = ['Manager', 'TeamLead']

    def form_valid(self, form):
        project = get_object_or_404(Project, pk=self.kwargs.get('pk'))
        user = form.save(commit=False)
        user.project = project
        user.save()
        form.save_m2m()
        return redirect('project_detail', pk=project.pk)

    def has_permission(self):
        return Project.objects.filter(user=self.request.user, pk=self.get_object().pk) and super().has_permission()

