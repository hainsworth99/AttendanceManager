from django.db import models


class CompetitionRecord(models.Model):
    date = models.DateField()  # date of the competition
    name = models.CharField(max_length=250)  # name of the competition
    student_id = models.IntegerField()  # student ID of the user associated with the record
