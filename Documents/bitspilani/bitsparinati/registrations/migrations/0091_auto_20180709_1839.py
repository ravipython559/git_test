# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2018-07-09 13:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registrations', '0090_auto_20180709_1638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otherfeepayment',
            name='full_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]