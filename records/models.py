from django.db import models


class AttendanceRecord(models.Model):
    student_id = models.IntegerField()  # student ID of the user assoociated with the record
    date = models.DateField()


class CompetitionRecord(models.Model):
    date = models.DateField()  # date of the competition
    name = models.CharField(max_length=250)  # name of the competition
    student_id = models.IntegerField()  # student ID of the user associated with the record


class FundraisingRecord(models.Model):
    name = models.CharField(max_length=250)  # name of the fundraising event
    date = models.DateField()  # date of the event
    student_id = models.IntegerField()  # student ID of the user associated with the record