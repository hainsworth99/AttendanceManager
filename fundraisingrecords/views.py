from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin


from .models import FundraisingRecord


class FundraisingRecordsListView(LoginRequiredMixin, ListView):
    model = FundraisingRecord
    template_name = 'fundraising_records.html'
