from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse
from django.views.generic import UpdateView
from webapp.models import Task
from webapp.forms import TaskForm


class TaskUpdateView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    template_name = 'tasks/update.html'
    form_class = TaskForm
    model = Task
    context_object_name = 'task'
    permission_required = 'webapp.change_task'

    def get_success_url(self):
        return reverse('task_detail', kwargs={'pk': self.object.pk})

    def has_permission(self):
        task = self.get_object()
        return super().has_permission() and self.request.user in task.project.user.all()

