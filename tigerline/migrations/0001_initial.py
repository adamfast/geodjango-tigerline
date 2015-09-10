# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='County',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('state_fips_code', models.CharField(max_length=b'2', verbose_name=b'State FIPS Code')),
                ('fips_code', models.CharField(max_length=3, verbose_name=b'FIPS Code')),
                ('county_identifier', models.CharField(max_length=5)),
                ('name', models.CharField(max_length=100)),
                ('name_and_description', models.CharField(max_length=100)),
                ('legal_statistical_description', models.CharField(max_length=2)),
                ('fips_55_class_code', models.CharField(max_length=2)),
                ('feature_class_code', models.CharField(max_length=5)),
                ('functional_status', models.CharField(max_length=1)),
                ('mpoly', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
            options={
                'verbose_name_plural': 'Counties',
            },
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fips_code', models.CharField(max_length=2, verbose_name=b'FIPS Code')),
                ('usps_code', models.CharField(max_length=2, verbose_name=b'USPS state abbreviation', db_index=True)),
                ('name', models.CharField(max_length=100, db_index=True)),
                ('area_description_code', models.CharField(max_length=2)),
                ('feature_class_code', models.CharField(max_length=5)),
                ('functional_status', models.CharField(max_length=1)),
                ('mpoly', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Zipcode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=5, db_index=True)),
                ('mpoly', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
            options={
                'ordering': ['code'],
            },
        ),
    ]
