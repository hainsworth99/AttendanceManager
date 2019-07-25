from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    is_admin = models.BooleanField(default=False)  # boolean that will give some admin privileges to certain users
    student_id = models.IntegerField(null=True)