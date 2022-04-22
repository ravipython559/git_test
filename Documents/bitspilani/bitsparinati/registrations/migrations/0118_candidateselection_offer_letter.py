# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2019-10-14 08:38
from __future__ import unicode_literals

from django.db import migrations, models
import registrations.models


class Migration(migrations.Migration):

    dependencies = [
        ('registrations', '0117_auto_20191014_1407'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidateselection',
            name='offer_letter',
            field=models.FileField(blank=True, max_length=1000, null=True, upload_to=registrations.models.user_directory_path, verbose_name='Offer Letter'),
        ),
    ]