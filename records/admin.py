from django.contrib import admin


from .models import AttendanceRecord, CompetitionRecord, FundraisingRecord


class AttendanceRecordAdmin(admin.ModelAdmin):
    list_display = ("id", "student_id", "date")


class CompetitionRecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'student_id', 'name', 'date')


class FundraisingRecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'student_id', 'name', 'date',)


admin.site.register(AttendanceRecord, AttendanceRecordAdmin)
admin.site.register(CompetitionRecord, CompetitionRecordAdmin)
admin.site.register(FundraisingRecord, FundraisingRecordAdmin)

