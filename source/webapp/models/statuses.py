from django.db import models


class Status(models.Model):
    status_title = models.CharField(
        max_length=100,
        null=False,
        verbose_name="Status")

    def __str__(self):
        return f'{self.status_title}'

