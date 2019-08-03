from django.contrib import admin


from .models import AttendanceRecord


class AttendanceRecordAdmin(admin.ModelAdmin):
    list_display = ("id", "student_id", "date")


admin.site.register(AttendanceRecord, AttendanceRecordAdmin)