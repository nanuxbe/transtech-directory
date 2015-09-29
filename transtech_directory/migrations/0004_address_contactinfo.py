# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('transtech_directory', '0003_auto_20150920_1306'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('street', models.CharField(max_length=255)),
                ('street2', models.CharField(max_length=255, blank=True, null=True)),
                ('city', models.CharField(max_length=100)),
                ('postal_code', models.CharField(max_length=10, blank=True, null=True)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('longitude', models.FloatField(blank=True, null=True)),
                ('latitude', models.FloatField(blank=True, null=True)),
                ('directory', models.ForeignKey(to='transtech_directory.Directory', related_name='addresses')),
            ],
        ),
        migrations.CreateModel(
            name='ContactInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('type', models.CharField(max_length=5, choices=[('phone', 'Phone'), ('email', 'E-Mail'), ('other', 'Other')])),
                ('directory', models.ForeignKey(to='transtech_directory.Directory', related_name='contacts')),
            ],
        ),
    ]
