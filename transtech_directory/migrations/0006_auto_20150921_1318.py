# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transtech_directory', '0005_auto_20150921_1047'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='address',
            options={'verbose_name_plural': 'addresses'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'categories'},
        ),
        migrations.AlterModelOptions(
            name='directory',
            options={'verbose_name_plural': 'directories'},
        ),
        migrations.AddField(
            model_name='directory',
            name='description',
            field=models.TextField(null=True, blank=True, verbose_name='Description'),
        ),
    ]
