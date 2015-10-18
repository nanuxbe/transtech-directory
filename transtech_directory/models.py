from django.db import models
from django.utils.translation import ugettext as _
from django.utils.text import slugify

from django_countries.fields import CountryField


CONTACT_TYPES = (
    ('phone', _('Phone')),
    ('email', _('E-Mail')),
    ('other', _('Other')),
)


class Category(models.Model):

    class Meta:
        verbose_name_plural = "categories"

    name = models.CharField(_('Category name'), max_length=100)
    slug = models.SlugField(_('Slug'), max_length=100)

    def __str__(self):
        return self.name


class Directory(models.Model):

    class Meta:
        verbose_name_plural = "directories"

    service_provider = models.CharField(_('Service provider name'), max_length=255)
    slug = models.SlugField(_('slug'), max_length=255)
    description = models.TextField(_('Description'), blank=True, null=True)
    service_category = models.ManyToManyField(Category, verbose_name=_('Categories'))
    link = models.URLField(_('Link'), blank=True, null=True)

    def __str__(self):
        return self.service_provider

    def categories(self):
        return ', '.join([c.name for c in self.service_category.all()])

    def short_description(self):
        if self.description is not None and len(self.description) > 30:
            return '{} ...'.format(self.description[:26])
        return self.description or ''

    def save(self, *args, **kwargs):
        # FIXME: check that the generated slug doesn't already exist in DB
        if self.slug is None:
            self.slug = slugify(self.service_provider)
        super(Directory, self).save(*args, **kwargs)


class ContactInfo(models.Model):

    directory = models.ForeignKey(Directory, verbose_name=_('Service provider'), related_name='contacts')
    type = models.CharField(_('Type'), max_length=5, choices=CONTACT_TYPES)
    value = models.CharField(_('Value'), max_length=400)

    def __str__(self):
        return self.directory.__str__() + " " + self.type


class Address(models.Model):

    class Meta:
        verbose_name_plural = "addresses"

    directory = models.ForeignKey(Directory, verbose_name=('Service provider'), related_name='addresses')
    street = models.CharField(_('Street address'), max_length=255)
    street2 = models.CharField(_('Second line'), max_length=255, blank=True, null=True)
    city = models.CharField(_('City'), max_length=100)
    postal_code = models.CharField(_('postal_code'), max_length=10, blank=True, null=True)
    country = CountryField(verbose_name=_('Country'))

    longitude = models.FloatField(_('Longitude'), blank=True, null=True)
    latitude = models.FloatField(_('Latitude'), blank=True, null=True)

    def __str__(self):
        return "%s, %s, %s, %s" % (self.street, self.street2, self.city, self.postal_code)
