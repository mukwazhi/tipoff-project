# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-30 16:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reporting', '0002_reportingindividual'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reportingindividual',
            name='report_no',
        ),
        migrations.AddField(
            model_name='incidentreport',
            name='Full_Name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='incidentreport',
            name='Phone_no',
            field=models.CharField(blank=True, max_length=100, null=100),
        ),
        migrations.AddField(
            model_name='incidentreport',
            name='Position_Title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='incidentreport',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.DeleteModel(
            name='reportingIndividual',
        ),
    ]
