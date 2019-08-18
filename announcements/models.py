from django.db import models


class Announcement(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
