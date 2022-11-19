from django.db import models
from django.core.exceptions import ValidationError


def at_summary_capitalize(value):
    if value != value.capitalize():
        raise ValidationError('Invalid (not capitalized) value')
    return value


class Task(models.Model):
    summary = models.CharField(
        max_length=300,
        null=False,
        blank=False,
        verbose_name='Summary',
        validators=[at_summary_capitalize]
    )
    description = models.TextField(
        max_length=3000,
        null=True,
        blank=True,
        verbose_name='Description'
    )
    status = models.ForeignKey(
        to='webapp.Status',
        related_name='status',
        on_delete=models.PROTECT,
        verbose_name='Status'
    )
    type = models.ManyToManyField(
        to='webapp.Type',
        related_name='type',
        blank=False
    )
    project = models.ForeignKey(
        to='webapp.Project',
        related_name='tasks',
        on_delete=models.CASCADE,
        verbose_name='Project'
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated at")

    def __str__(self):
        return f"{self.summary}-{self.status}"

