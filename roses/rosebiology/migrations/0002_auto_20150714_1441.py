# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rosebiology', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('url', models.CharField(max_length=1024)),
            ],
        ),
        migrations.CreateModel(
            name='Reference',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('url', models.CharField(max_length=1024)),
            ],
        ),
        migrations.AlterModelOptions(
            name='species',
            options={'verbose_name_plural': 'species'},
        ),
        migrations.AlterModelOptions(
            name='subspecies',
            options={'verbose_name_plural': 'subspecies'},
        ),
        migrations.AddField(
            model_name='species',
            name='further_reference',
            field=models.ManyToManyField(to='rosebiology.Reference', blank=True),
        ),
        migrations.AddField(
            model_name='species',
            name='image',
            field=models.ManyToManyField(to='rosebiology.Image', blank=True),
        ),
    ]
