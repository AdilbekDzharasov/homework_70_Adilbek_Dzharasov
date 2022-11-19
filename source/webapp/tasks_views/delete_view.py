from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from webapp.models import Task
from django.views.generic import DeleteView


class TaskDeleteView(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    template_name = 'tasks/delete.html'
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('task_home')
    permission_required = 'webapp.delete_task'

    def has_permission(self):
        task = self.get_object()
        return super().has_permission() and self.request.user in task.project.user.all()

