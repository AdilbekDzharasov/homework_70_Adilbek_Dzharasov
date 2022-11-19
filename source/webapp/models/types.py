from django.db import models


class Type(models.Model):
    type_title = models.CharField(
        max_length=100,
        null=False,
        verbose_name="Type")

    def __str__(self):
        return f'{self.type_title}'

