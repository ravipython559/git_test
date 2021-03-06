# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-11-07 06:36
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registrations', '0054_auto_20171027_2318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='program',
            name='document_upload_page_path',
            field=models.CharField(blank=True, choices=[(None, 'Choose Document To Upload'), ('guidelines_document/oracle.html', 'Oracle'), ('guidelines_document/wipro.html', 'Wipro'), ('guidelines_document/certification_programs.html', 'Certification Programs')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='studentcandidateapplication',
            name='login_email',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='studentcandidateapplication_requests_created_5', to=settings.AUTH_USER_MODEL, unique=True),
        ),
    ]
