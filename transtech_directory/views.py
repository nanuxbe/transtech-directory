
from django.views.generic import ListView, DetailView, CreateView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .forms import DirectoryForm
from .models import Directory


class DirectoryListView(ListView):
    model = Directory


class DirectoryDetailView(DetailView):
    model = Directory


class DirectoryCreateView(CreateView):
    model = Directory()
    success_url = reverse_lazy('directory')
    template_name = 'transtech_directory/create.html'
    form_class = DirectoryForm 

    def form_valid(self, form):
        form.save()
        # Add google api call task
        return super(DirectoryCreateView, self).form_valid(form)

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(DirectoryCreateView, self).dispatch(request, *args, **kwargs)
