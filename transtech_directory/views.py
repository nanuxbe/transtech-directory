from django.views.generic import ListView
from django.shortcuts import render
from .forms import DirectoryForm
from .models import Directory


class DirectoryListView(ListView):
    model = Directory

def directory_form(request):
    return render(request, 'directory_form.html', {'form': DirectoryForm()})