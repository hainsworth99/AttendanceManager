from django.urls import path


from .views import FundraisingRecordsListView


urlpatterns = [
    path('', FundraisingRecordsListView.as_view(), name='fundraising_records')
]