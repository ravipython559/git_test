# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2019-08-07 09:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registrations', '0109_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentcandidateapplication',
            name='programming_flag',
            field=models.CharField(blank=True, choices=[('True', 'Yes'), ('False', 'No')], max_length=10, null=True),
        ),
    ]
