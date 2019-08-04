from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin


from .models import AttendanceRecord, CompetitionRecord, FundraisingRecord


class AttendanceRecordsListView(LoginRequiredMixin, ListView):

    model = AttendanceRecord
    template_name = 'attendance_records.html'


class CompetitionRecordsListView(LoginRequiredMixin, ListView):

    model = CompetitionRecord
    template_name = 'competition_records.html'


class FundraisingRecordsListView(LoginRequiredMixin, ListView):

    model = FundraisingRecord
    template_name = 'fundraising_records.html'