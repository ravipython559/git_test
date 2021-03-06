# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2021-05-28 13:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registrations', '0147_auto_20210511_1531'),
    ]

    operations = [
        migrations.AddField(
            model_name='bitsuser',
            name='utm_campaign_first',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='bitsuser',
            name='utm_campaign_last',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='bitsuser',
            name='utm_medium_first',
            field=models.CharField(blank=True, max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='bitsuser',
            name='utm_medium_last',
            field=models.CharField(blank=True, max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='bitsuser',
            name='utm_source_first',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='bitsuser',
            name='utm_source_last',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
