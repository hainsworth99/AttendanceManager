from django.views.generic import ListView

from .models import AttendanceRecord

class AttendanceRecordsListView(ListView):
    model = AttendanceRecord
