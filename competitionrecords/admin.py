from django.contrib import admin


from .models import CompetitionRecord


class CompetitionRecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'student_id', 'name', 'date')


admin.site.register(CompetitionRecord, CompetitionRecordAdmin)