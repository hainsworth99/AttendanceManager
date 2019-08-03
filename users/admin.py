from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['id', 'username', 'email', 'first_name', 'last_name', 'student_id', 'training_group', 'is_staff']


admin.site.register(CustomUser, CustomUserAdmin)
