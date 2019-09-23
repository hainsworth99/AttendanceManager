from django.urls import path


from .views import TrainingGroupListView


urlpatterns = [
    path('', TrainingGroupListView.as_view(), name='training_groups')
]