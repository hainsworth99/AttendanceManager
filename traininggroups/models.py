from django.db import models
from django.contrib.postgres.fields import ArrayField


class TrainingGroup(models.Model):
    name = models.CharField(max_length=100)
    group_members = ArrayField(models.CharField(max_length=250), null=True)

    def __str__(self):
        return self.name
