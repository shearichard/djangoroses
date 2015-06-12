# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rosebiology', '0003_auto_20150714_1445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='species',
            name='subspecies',
            field=models.ForeignKey(to='rosebiology.Subspecies', null=True, blank=True),
        ),
    ]
