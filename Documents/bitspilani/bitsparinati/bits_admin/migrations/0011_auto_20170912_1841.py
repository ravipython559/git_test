# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-09-12 13:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bits_admin', '0010_auto_20170912_1839'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicantexceptionsarchived',
            name='run',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='exceptionlistorgapplicantsarchived',
            name='run',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
    ]
