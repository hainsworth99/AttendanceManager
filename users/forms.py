from django.forms import ModelForm
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


class CustomUserChangeForm(ModelForm):

    class Meta:
        model = CustomUser
        fields = (
            'first_name',
            'last_name',
            'email',
            'student_id',
        )