# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2018-12-18 08:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('semester_api', '0002_auto_20180725_1623'),
    ]

    operations = [
        migrations.AddField(
            model_name='semzestemitransaction',
            name='cancelled_on',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='semzestemitransaction',
            name='is_cancelled',
            field=models.BooleanField(default=False),
        ),
    ]
