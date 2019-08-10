from rest_framework import generics, permissions


from records.models import AttendanceRecord
from .serializers import AttendanceRecordSerializer


class AttedanceRecordList(generics.ListCreateAPIView):  # api view that allows GET and POST
    queryset = AttendanceRecord.objects.all()
    serializer_class = AttendanceRecordSerializer
    permission_classes = (permissions.IsAdminUser,)  # only admin users may use


class AttedanceRecordDetail(generics.RetrieveUpdateDestroyAPIView):  # api view that allows POST, GET, PUT, DELETE
    queryset = AttendanceRecord.objects.all()
    serializer_class = AttendanceRecordSerializer
    permission_classes = (permissions.IsAdminUser,)  # only admin users may use
