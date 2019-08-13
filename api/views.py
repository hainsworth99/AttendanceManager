from rest_framework.response import Response
from rest_framework import generics, permissions
from rest_framework.status import (
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST,
    HTTP_200_OK,
    HTTP_500_INTERNAL_SERVER_ERROR,
)


from records.models import AttendanceRecord
from .serializers import AttendanceRecordSerializer


class AttedanceRecordList(generics.ListCreateAPIView):  # api view that allows GET and POST
    queryset = AttendanceRecord.objects.all()
    serializer_class = AttendanceRecordSerializer
    permission_classes = (permissions.IsAdminUser,)  # only admin users may use

    # overriding the view's POST method
    # use of this system requires 'unique' attendance records, i. no two records can have both same s_id and same date
    # this prevents users from recording their attendance twice for the same day
    def post(self, request):
        student_id = request.data.get('student_id')
        date = request.data.get('date')

        # ensure request provides the necessary parameters
        if not student_id or not date:
            return Response({'Error': 'Please provide a student id and date.'}, status=HTTP_400_BAD_REQUEST)

        # ensure new record will be 'unique'
        for record in AttendanceRecord.objects.all():
            if str(record.student_id) == str(student_id) and str(record.date) == str(date):
                return Response({'Success': 'Attendance record already exists, nothing to do.'}, status=HTTP_200_OK)

        # create new attendance record
        try:
            new_record = AttendanceRecord.objects.create(student_id=student_id, date=date)
            new_record.save()
        except:
            return Response({'Error': 'Something went wrong.'}, status=HTTP_500_INTERNAL_SERVER_ERROR)
        return Response({'Success': 'Attendance record created.'}, status=HTTP_201_CREATED)


class AttedanceRecordDetail(generics.RetrieveUpdateDestroyAPIView):  # api view that allows GET, PUT, DELETE
    queryset = AttendanceRecord.objects.all()
    serializer_class = AttendanceRecordSerializer
    permission_classes = (permissions.IsAdminUser,)  # only admin users may use
