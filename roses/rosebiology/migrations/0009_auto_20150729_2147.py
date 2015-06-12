# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rosebiology', '0008_auto_20150727_1735'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='species',
            options={'verbose_name_plural': 'species', 'permissions': (('display_details_species_', 'Can view details of a Species'),)},
        ),
    ]
