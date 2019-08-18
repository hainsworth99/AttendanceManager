from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin


from .models import AttendanceRecord, CompetitionRecord, FundraisingRecord


# needed new class bc django templates cannot call tuple/dictionary indexes in tags, which would have been far easier
class UserListRecord:

    date = None
    attended = None

    def __init__(self, date, attended):
        self.date = date
        self.attended = attended


class AttendanceRecordsListView(LoginRequiredMixin, ListView):

    model = AttendanceRecord
    template_name = 'attendance_records.html'

    def get_user(self):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super(AttendanceRecordsListView, self).get_context_data(**kwargs)

        # get attendance dates from user records
        user = self.get_user()
        user_attendance_dates = []
        for record in context['object_list']:
            if record.student_id == user.student_id:
                user_attendance_dates.append(record.date)

        context['user_attendance_num'] = len(user_attendance_dates)

        # get unique dates from all attendance records
        unique_dates = []
        for record in context['object_list']:
            if record.date not in unique_dates:
                unique_dates.append(record.date)

        context['total_dates'] = len(unique_dates)

        context['attendance_percentage'] = int(context['user_attendance_num']/context['total_dates']*100)

        # create object containing user's attendance status for each date
        user_attendace_list = []
        for date in unique_dates:
            user_attendace_list.append(UserListRecord(date, date in user_attendance_dates))

        print(user_attendace_list)

        context['user_attendance_list'] = user_attendace_list

        return context


class CompetitionRecordsListView(LoginRequiredMixin, ListView):

    model = CompetitionRecord
    template_name = 'competition_records.html'

    def get_user(self):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super(CompetitionRecordsListView, self).get_context_data(**kwargs)

        # get user and user records
        user = self.get_user()
        user_records = []
        for record in context['object_list']:
            if record.student_id == user.student_id:
                user_records.append(record)

        context['user_competition_list'] = user_records
        context['user_competition_number'] = len(user_records)

        return context


class FundraisingRecordsListView(LoginRequiredMixin, ListView):

    model = FundraisingRecord
    template_name = 'fundraising_records.html'

    def get_user(self):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super(FundraisingRecordsListView, self).get_context_data(**kwargs)

        # get user and user records
        user = self.get_user()
        user_records = []
        for record in context['object_list']:
            if record.student_id == user.student_id:
                user_records.append(record)

        context['user_fundraising_list'] = user_records
        context['user_fundraising_number'] = len(user_records)

        return context
