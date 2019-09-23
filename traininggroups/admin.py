from django.contrib import admin


from .models import TrainingGroup


class TrainingGroupAdmin(admin.ModelAdmin):
    list_display = ("name", "group_members")


admin.site.register(TrainingGroup)
