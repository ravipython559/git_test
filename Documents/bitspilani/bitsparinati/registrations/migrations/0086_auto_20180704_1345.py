# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2018-07-04 08:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registrations', '0085_auto_20180625_1324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='programdocumentmap',
            name='deffered_submission_flag',
            field=models.BooleanField(default=False, verbose_name='Deferred Submission Flag'),
        ),
    ]
