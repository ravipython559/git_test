# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2020-04-29 16:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registrations', '0122_auto_20200319_1828'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProgramFormNotesFields',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notes', models.TextField(verbose_name='Form Notes')),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='programformnotesfields_pg', to='registrations.Program')),
            ],
            options={
                'verbose_name': 'Program Form Notes',
                'verbose_name_plural': 'Program Form Notes',
            },
        ),
    ]