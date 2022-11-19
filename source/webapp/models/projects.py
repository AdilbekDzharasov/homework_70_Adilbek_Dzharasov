from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models
from webapp.managers import ProjectManager


class Project(models.Model):
    title = models.CharField(
        max_length=300,
        null=False,
        blank=False,
        verbose_name='Title'
    )
    description = models.TextField(
        max_length=3000,
        null=True,
        blank=True,
        verbose_name='Description'
    )
    is_deleted = models.BooleanField(verbose_name='Is deleted', default=False, null=False)
    beginning_date = models.DateField(verbose_name='Beginning date', null=False, blank=False)
    expiration_date = models.DateField(verbose_name='Expiration date', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")
    deleted_at = models.DateTimeField(verbose_name='Deleted at', null=True, default=None)
    user = models.ManyToManyField(User, related_name='projects', blank=True, verbose_name='User')
    is_deleted_user = models.BooleanField(verbose_name='Is deleted user', default=False, null=False)

    objects = ProjectManager()

    def delete(self, using=None, keep_parents=False):
        self.deleted_at = timezone.now()
        self.is_deleted = True
        self.save()

    def __str__(self):
        return f"{self.title}"

