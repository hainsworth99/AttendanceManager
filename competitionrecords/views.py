from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin


from .models import CompetitionRecord


class CompetitionRecordsListView(LoginRequiredMixin, ListView):

    model = CompetitionRecord
    template_name = 'competition_records.html'
