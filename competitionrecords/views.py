from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

class CompetitionRecordsListView(LoginRequiredMixin, ListView):
    foo = 0
