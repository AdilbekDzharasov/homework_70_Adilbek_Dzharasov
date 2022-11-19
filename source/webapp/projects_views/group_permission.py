from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class GroupPermission(UserPassesTestMixin):
    groups = []

    def test_func(self):
        return self.request.user.groups.filter(name__in=self.groups).exists()
