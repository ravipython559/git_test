# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-03-06 06:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registrations', '0022_auto_20170306_1202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='program',
            name='show_to_fee_wvr_appl_flag',
            field=models.BooleanField(default=False, verbose_name='Show Program to Applicants with fee waivers in other Programs'),
        ),
    ]
