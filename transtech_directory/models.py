from django.db import models

from django_countries.fields import CountryField


CONTACT_TYPES = (
    ('phone', 'Phone'),
    ('email', 'E-Mail'),
    ('other', 'Other'),
)


class Category(models.Model):

    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)


class Directory(models.Model):

    service_provider = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    service_category = models.ManyToManyField(Category)
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.service_provider


class ContactInfo(models.Model):

    directory = models.ForeignKey(Directory, related_name='contacts')
    type = models.CharField(max_length=5, choices=CONTACT_TYPES)


class Address(models.Model):

    directory = models.ForeignKey(Directory, related_name='addresses')
    street = models.CharField(max_length=255)
    street2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=10, blank=True, null=True)
    country = CountryField()

    longitude = models.FloatField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
