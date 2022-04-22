# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2019-04-12 13:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bits_admin', '0034_auto_20190412_1810'),
    ]

    operations = [
        migrations.CreateModel(
            name='DegreeArchived',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree_short_name', models.CharField(blank=True, max_length=30, null=True)),
                ('degree_long_name', models.CharField(blank=True, max_length=45, null=True)),
                ('qualification_category', models.CharField(blank=True, max_length=70, null=True)),
            ],
        ),
    ]