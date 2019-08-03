from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import AttendanceRecord


class AttendanceRecordsListView(LoginRequiredMixin, ListView):

    model = AttendanceRecord
    template_name = 'attendance_records.html'
