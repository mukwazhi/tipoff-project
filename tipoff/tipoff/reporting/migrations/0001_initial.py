# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-25 12:13
from __future__ import unicode_literals

from django.db import migrations, models
import reporting.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IncidentReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report_no', models.CharField(blank=True, default=reporting.models.report_number, max_length=500, null=True)),
                ('nature_of_report', models.CharField(choices=[('Smuggling', 'Smuggling'), ('Fraud', 'Fraud'), ('Extortion', 'Extortion'), ('Bribery', 'Bribery'), ('Corruption', 'Corruption'), ('Misappropriation', 'Misappropriation'), ('Other', 'Other')], default=0, max_length=20)),
                ('date_of_incident', models.DateField()),
                ('time_of_incident', models.TimeField()),
                ('location_of_incident', models.CharField(max_length=100)),
                ('specific_location', models.CharField(max_length=100)),
                ('name_of_party_involved', models.CharField(blank=True, max_length=100, null=True)),
                ('organisation', models.CharField(blank=True, max_length=100, null=True)),
                ('gender', models.CharField(blank=True, max_length=100, null=True)),
                ('role', models.CharField(blank=True, max_length=100, null=True)),
                ('incident_detail', models.TextField(max_length=3000)),
                ('upload_evidence', models.FileField(blank=True, null=True, upload_to=b'')),
            ],
        ),
    ]
