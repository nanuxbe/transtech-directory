from django.db import models

from django_countries.fields import CountryField


CONTACT_TYPES = (
    ('phone', 'Phone'),
    ('email', 'E-Mail'),
    ('other', 'Other'),
)


class Category(models.Model):

    class Meta:
        verbose_name_plural = "categories"

    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)

    def __str__(self): 
        return self.name

class Directory(models.Model):

    class Meta:
        verbose_name_plural = "directories"

    service_provider = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    service_category = models.ManyToManyField(Category)
    link = models.URLField(blank=True, null=True)

    def __str__(self): 
        return self.service_provider


class ContactInfo(models.Model):

    directory = models.ForeignKey(Directory, related_name='contacts')
    type = models.CharField(max_length=5, choices=CONTACT_TYPES)

    def __str__(self): 
        return self.directory.__str__() + " " + self.type

class Address(models.Model):

    class Meta:
        verbose_name_plural = "addresses"

    directory = models.ForeignKey(Directory, related_name='addresses')
    street = models.CharField(max_length=255)
    street2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=10, blank=True, null=True)
    country = CountryField()

    longitude = models.FloatField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)

    def __str__(self): 
        return "%s, %s, %s, %s" % (self.street, self.street2, self.city, self.postal_code)