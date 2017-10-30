
from django.views.generic import ListView, DetailView, CreateView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .forms import DirectoryForm, AddressFormset, AddressHelper, ContactInfoFormset, ContactInfoHelper
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

    def get_context_data(self, **kwargs):
        context = super(DirectoryCreateView, self).get_context_data(**kwargs)
        address_form_kwargs = {}
        contact_form_kwargs = {}
        if self.request.method == 'POST':
            address_form_kwargs['data'] = self.request.POST
            contact_form_kwargs['data'] = self.request.POST
        context['address_form'] = AddressFormset(**address_form_kwargs)
        context['contact_form'] = ContactInfoFormset(**contact_form_kwargs)
        context['address_helper'] = AddressHelper()
        context['contact_helper'] = ContactInfoHelper()
        return context

    # def get_success_url(self):
    #     return reverse_lazy('directory_detail', kwargs={'slug': self._slug})

    def form_valid(self, form):
        address_form = AddressFormset(data=self.request.POST)
        contact_form = ContactInfoFormset(data=self.request.POST)

        for a_form in address_form:
            if not a_form.data['{}-DELETE'.format(a_form.prefix)] and not a_form.is_valid():
                return self.form_invalid(form)
        for c_form in contact_form:
            if not c_form.data['{}-DELETE'.format(c_form.prefix)] and not c_form.is_valid():
                return self.form_invalid(form)

        form.save()
        for a_form in address_form:
            if not a_form.data['{}-DELETE'.format(a_form.prefix)]:
                a_obj = a_form.instance
                a_obj.directory = form.instance
                a_obj.save()
        for c_form in contact_form:
            if not c_form.data['{}-DELETE'.format(c_form.prefix)]:
                c_obj = c_form.instance
                c_obj.directory = form.instance
                c_obj.save()

        self._slug = form.instance.slug

        return super(DirectoryCreateView, self).form_valid(form)

    # @method_decorator(login_required)
    # def dispatch(self, request, *args, **kwargs):
    #     return super(DirectoryCreateView, self).dispatch(request, *args, **kwargs)
