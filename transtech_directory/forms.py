from django.forms import ModelForm
from django.forms.models import formset_factory

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset

from .models import Address, ContactInfo, Directory


class AddressForm(ModelForm):

    class Meta:
        model = Address
        fields = (
            'street',
            'city',
            'postal_code',
            'country',
        )


AddressFormset = formset_factory(AddressForm, can_delete=True)


class AddressHelper(FormHelper):

    def __init__(self, *args, **kwargs):
        super(AddressHelper, self).__init__(*args, **kwargs)

        self.label_class = 'col-md-3 col-sm-4 col-xs-12'
        self.field_class = 'col-md-9 col-sm-8 col-xs-12'
        self.form_tag = False

        self.layout = Layout(
            'street',
            'city',
            'postal_code',
            'country',
        )


class ContactInfoForm(ModelForm):

    class Meta:
        model = ContactInfo
        fields = (
            'type',
            'value'
        )


ContactInfoFormset = formset_factory(ContactInfoForm, can_delete=True)


class ContactInfoHelper(FormHelper):

    def __init__(self, *args, **kwargs):
        super(ContactInfoHelper, self).__init__(*args, **kwargs)

        self.label_class = 'col-md-3 col-sm-4 col-xs-12'
        self.field_class = 'col-md-9 col-sm-8 col-xs-12'
        self.form_tag = False

        self.layout = Layout(
            'type',
            'value'
        )


class DirectoryForm(ModelForm):

    class Meta:
        model = Directory
        fields = (
            'service_provider',
            'description',
            'service_category',
            'link',
        )

    def __init__(self, *args, **kwargs):
        super(DirectoryForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()

        self.helper.label_class = 'col-md-3 col-sm-4 col-xs-12'
        self.helper.field_class = 'col-md-9 col-sm-8 col-xs-12'
        self.helper.form_tag = False

        self.helper.layout = Layout(
            Fieldset(
                'Add a new service provider',
                'service_provider',
                'description',
                'service_category',
                'link',
            # ),
            # ButtonHolder(
            #     Submit('submit', 'Create', css_class='btn btn-primary')
            )
        )
