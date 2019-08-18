from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin


from .models import Announcement


class AnnouncementListView(ListView):

    model = Announcement
    template_name = 'home.html'
