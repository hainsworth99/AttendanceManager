from django.db import models


class AttendanceRecord(models.Model):
    student_id = models.IntegerField()
    date = models.DateField()