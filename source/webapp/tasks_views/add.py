from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import CreateView
from webapp.models import Task
from webapp.forms import TaskForm
from django.views.generic.detail import DetailView
from webapp.models.projects import Project
from webapp.forms import ProjectTaskForm


class TaskAddView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    model = Task
    template_name = 'tasks/add.html'
    form_class = TaskForm
    permission_required = 'webapp.create_task'

    def get_success_url(self):
        return reverse('task_detail', kwargs={'pk': self.object.pk})

    def test_func(self):
        return self.get_object().user == self.request.user or self.request.user.has_perm('webapp.create_task')


class ProjectTaskAddView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    model = Task
    template_name = 'tasks/project_task_add.html'
    form_class = ProjectTaskForm
    permission_required = 'webapp.add_task'

    def form_valid(self, form):
        project = get_object_or_404(Project, pk=self.kwargs.get('pk'))
        task = form.save(commit=False)
        task.project = project
        task.save()
        form.save_m2m()
        return redirect('project_detail', pk=project.pk)

    def has_permission(self):
        project = get_object_or_404(Project, pk=self.kwargs.get('pk'))
        return super().has_permission() and self.request.user in project.user.all()


class TaskDetailView(DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'tasks/task.html'

