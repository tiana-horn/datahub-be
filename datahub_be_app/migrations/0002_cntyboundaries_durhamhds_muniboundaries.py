# Generated by Django 2.0.5 on 2018-05-30 00:25

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datahub_be_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='cntyboundaries',
            fields=[
                ('ogc_fid', models.IntegerField(primary_key=True, serialize=False)),
                ('wkb_geometry', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
                ('fips', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='durhamhds',
            fields=[
                ('ogc_fid', models.IntegerField(primary_key=True, serialize=False)),
                ('wkb_geometry', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
                ('name', models.CharField(max_length=100)),
                ('shape_area', models.DecimalField(decimal_places=15, max_digits=20)),
            ],
        ),
        migrations.CreateModel(
            name='muniboundaries',
            fields=[
                ('ogc_fid', models.IntegerField(primary_key=True, serialize=False)),
                ('wkb_geometry', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
                ('towncode', models.CharField(max_length=5)),
                ('municipalb', models.CharField(max_length=100)),
            ],
        ),
    ]
