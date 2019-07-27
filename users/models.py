from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

class CustomUser(AbstractUser):
    is_admin = models.BooleanField(default=False)  # boolean that will give some admin privileges to certain users
    student_id = models.IntegerField(null=True, blank=False)
    first_name = models.CharField(_('first name'), max_length=30, blank=False)
    last_name = models.CharField(_('last name'), max_length=150, blank=False)
    email = models.EmailField(_('email address'), blank=False)

    REQUIRED_FIELDS = ['email', 'student_id', 'first_name', 'last_name']