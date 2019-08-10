from rest_framework import serializers


from records.models import AttendanceRecord


class AttendanceRecordSerializer(serializers.ModelSerializer):  # serializer for the AttendanceRecord model
    class Meta:
        model = AttendanceRecord
        fields = ('id', 'student_id', 'date',)