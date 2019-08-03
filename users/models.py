from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

class CustomUser(AbstractUser):
    student_id = models.IntegerField(null=True, blank=False)
    first_name = models.CharField(_('first name'), max_length=30, blank=False)
    last_name = models.CharField(_('last name'), max_length=150, blank=False)
    email = models.EmailField(_('email address'), blank=False)
    training_group = models.IntegerField(null=True, blank=True)  # will allow automated training group sorting, 1-4 beginner-advanced

    REQUIRED_FIELDS = ['email', 'student_id', 'first_name', 'last_name']