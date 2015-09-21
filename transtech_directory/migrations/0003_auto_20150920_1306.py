# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transtech_directory', '0002_auto_20150920_1255'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='directory',
            name='link',
            field=models.URLField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='directory',
            name='slug',
            field=models.SlugField(max_length=255, default=' '),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='directory',
            name='service_category',
            field=models.ManyToManyField(to='transtech_directory.Category'),
        ),
    ]
