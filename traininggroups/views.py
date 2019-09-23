from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin


from .models import TrainingGroup


class TrainingGroupListView(LoginRequiredMixin, ListView):
    model = TrainingGroup
    template_name = 'training_groups.html'

    def get_context_data(self, **kwargs):
        context = super(TrainingGroupListView, self).get_context_data(**kwargs)
        return context
