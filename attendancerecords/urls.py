from django.urls import path


from .views import AttendanceRecordsListView


urlpatterns = [
    path('', AttendanceRecordsListView.as_view(), name='attendance_records')
]