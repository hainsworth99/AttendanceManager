from django.urls import path


from .views import SignUpView, UserUpdateView


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('update_user_info/<int:pk>/', UserUpdateView.as_view(), name='user_update'),
]