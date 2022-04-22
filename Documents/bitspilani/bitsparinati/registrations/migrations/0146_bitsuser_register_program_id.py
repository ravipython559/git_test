# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2021-05-06 12:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registrations', '0145_auto_20210224_1206'),
    ]

    operations = [
        migrations.AddField(
            model_name='bitsuser',
            name='register_program_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bitsuser_pgm', to='registrations.Program'),
        ),
    ]