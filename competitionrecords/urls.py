from django.urls import path


from .views import CompetitionRecordsListView


urlpatterns = [
    path('', CompetitionRecordsListView.as_view(), name='competition_records'),
]