from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm


from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):


    class Meta(UserCreationForm):
        model = CustomUser
        fields = (
            'first_name',
            'last_name',
            'username',
            'email',
            'student_id',
        )


class CustomUserChangeForm(UserChangeForm):


    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields