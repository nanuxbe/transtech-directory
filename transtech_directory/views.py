from django.views.generic import ListView

from .models import Directory


class DirectoryListView(ListView):
    model = Directory
