# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('rosebiology', '0007_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='species',
            name='created',
            field=models.DateTimeField(editable=False, default=datetime.datetime(2015, 1,  1, 0, 0, 0, 0, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='species',
            name='modified',
            field=models.DateTimeField(editable=False, default=datetime.datetime(2015, 1,  1, 0, 0, 0, 0, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
