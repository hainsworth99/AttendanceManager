from django.contrib import admin


from .models import FundraisingRecord


class FundraisingRecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'student_id', 'name', 'date',)


admin.site.register(FundraisingRecord, FundraisingRecordAdmin)
