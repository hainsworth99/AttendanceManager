from django.urls import path


from .views import AttendanceRecordsListView, CompetitionRecordsListView, FundraisingRecordsListView


urlpatterns = [
    path('attendance_records/', AttendanceRecordsListView.as_view(), name='attendance_records'),
    path('competition_records/', CompetitionRecordsListView.as_view(), name='competition_records'),
    path('fundraising_records/', FundraisingRecordsListView.as_view(), name='fundraising_records'),
]