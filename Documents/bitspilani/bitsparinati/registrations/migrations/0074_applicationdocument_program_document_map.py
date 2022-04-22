# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2018-06-14 19:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registrations', '0073_auto_20180611_1854'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicationdocument',
            name='program_document_map',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='applicationdocument_1', to='registrations.ProgramDocumentMap'),
        ),
    ]