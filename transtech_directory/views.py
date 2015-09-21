from django.views.generic import ListView, DetailView, CreateView
from django.core.urlresolvers import reverse_lazy

from .models import Directory


class DirectoryListView(ListView):
    model = Directory


class DirectoryDetailView(DetailView):
    model = Directory


class DirectoryCreateView(CreateView):
    model = Directory()
    success_url = reverse_lazy('directory')
    template_name = 'transtech_directory/create.html'

    def form_valid(self, form):
        form.save()
        # Add google api call tak
        return super(DirectoryCreateView, self).form_valid(form)
