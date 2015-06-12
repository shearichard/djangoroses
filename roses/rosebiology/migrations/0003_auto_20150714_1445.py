# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rosebiology', '0002_auto_20150714_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='url',
            field=models.URLField(max_length=1024),
        ),
        migrations.AlterField(
            model_name='reference',
            name='url',
            field=models.URLField(max_length=1024),
        ),
    ]
