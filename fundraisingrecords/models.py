from django.db import models


class FundraisingRecord(models.Model):
    name = models.CharField(max_length=250)  # name of the fundraising event
    date = models.DateField()  # date of the event
    student_id = models.IntegerField()  # student ID of the user associated with the record
