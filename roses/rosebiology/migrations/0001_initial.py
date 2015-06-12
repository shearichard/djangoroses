# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CommonName',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Range',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('continent', models.CharField(choices=[('AF', 'Africa'), ('AN', 'Antartica'), ('AS', 'Asia'), ('EU', 'Europe'), ('NA', 'North America'), ('OC', 'Oceania'), ('OT', 'Other')], max_length=2, default='OT')),
                ('place_description', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Species',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('binomial_nomenclature', models.CharField(max_length=200)),
                ('height_and_spread', models.CharField(max_length=100)),
                ('common_name', models.ManyToManyField(blank=True, to='rosebiology.CommonName')),
                ('range', models.ManyToManyField(blank=True, to='rosebiology.Range')),
            ],
        ),
        migrations.CreateModel(
            name='Subspecies',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Use',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='species',
            name='subspecies',
            field=models.ForeignKey(to='rosebiology.Subspecies', blank=True),
        ),
        migrations.AddField(
            model_name='species',
            name='use',
            field=models.ManyToManyField(blank=True, to='rosebiology.Use'),
        ),
    ]
