# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transtech_directory', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='directory',
            old_name='company',
            new_name='service_provider',
        ),
    ]
