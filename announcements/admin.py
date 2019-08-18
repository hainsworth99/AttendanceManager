from django.contrib import admin


from .models import Announcement


class AnnouncementRecordAdmin(admin.ModelAdmin):
    list_display = ("title", "body",)


admin.site.register(Announcement)
