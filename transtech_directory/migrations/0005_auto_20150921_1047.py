# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('transtech_directory', '0004_address_contactinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactinfo',
            name='value',
            field=models.CharField(verbose_name='Value', default=' ', max_length=400),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='address',
            name='city',
            field=models.CharField(verbose_name='City', max_length=100),
        ),
        migrations.AlterField(
            model_name='address',
            name='country',
            field=django_countries.fields.CountryField(verbose_name='Country', max_length=2),
        ),
        migrations.AlterField(
            model_name='address',
            name='directory',
            field=models.ForeignKey(related_name='addresses', verbose_name='Service provider', to='transtech_directory.Directory'),
        ),
        migrations.AlterField(
            model_name='address',
            name='latitude',
            field=models.FloatField(verbose_name='Latitude', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='longitude',
            field=models.FloatField(verbose_name='Longitude', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='postal_code',
            field=models.CharField(verbose_name='postal_code', max_length=10, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='street',
            field=models.CharField(verbose_name='Street address', max_length=255),
        ),
        migrations.AlterField(
            model_name='address',
            name='street2',
            field=models.CharField(verbose_name='Second line', max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(verbose_name='Category name', max_length=100),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(verbose_name='Slug', max_length=100),
        ),
        migrations.AlterField(
            model_name='contactinfo',
            name='directory',
            field=models.ForeignKey(related_name='contacts', verbose_name='Service provider', to='transtech_directory.Directory'),
        ),
        migrations.AlterField(
            model_name='contactinfo',
            name='type',
            field=models.CharField(verbose_name='Type', choices=[('phone', 'Phone'), ('email', 'E-Mail'), ('other', 'Other')], max_length=5),
        ),
        migrations.AlterField(
            model_name='directory',
            name='link',
            field=models.URLField(verbose_name='Link', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='directory',
            name='service_category',
            field=models.ManyToManyField(verbose_name='Categories', to='transtech_directory.Category'),
        ),
        migrations.AlterField(
            model_name='directory',
            name='service_provider',
            field=models.CharField(verbose_name='Service provider name', max_length=255),
        ),
        migrations.AlterField(
            model_name='directory',
            name='slug',
            field=models.SlugField(verbose_name='slug', max_length=255),
        ),
    ]
