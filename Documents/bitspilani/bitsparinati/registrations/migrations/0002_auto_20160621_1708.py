# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-21 11:38
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registrations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='degree',
            name='degree_long_name',
            field=models.CharField(max_length=45, validators=[django.core.validators.RegexValidator(code='invalid_degree_long_name', message='degree long name must be Alphanumeric', regex='^[\\w\\s_.()]+$')]),
        ),
        migrations.AlterField(
            model_name='degree',
            name='degree_short_name',
            field=models.CharField(max_length=30, unique=True, validators=[django.core.validators.RegexValidator(code='invalid_degree_short_name', message='degree short name must be Alphanumeric', regex='^[\\w\\s_.()]+$')]),
        ),
        migrations.AlterField(
            model_name='discpline',
            name='discipline_long_name',
            field=models.CharField(max_length=60, validators=[django.core.validators.RegexValidator(code='invalid_discipline_long_name', message='discipline long name must be Alphanumeric', regex='^[\\w\\s_.()]+$')]),
        ),
        migrations.AlterField(
            model_name='discpline',
            name='discipline_name',
            field=models.CharField(max_length=40, unique=True, validators=[django.core.validators.RegexValidator(code='invalid_discipline_name', message='discipline name must be Alphanumeric', regex='^[\\w\\s_.()]+$')]),
        ),
    ]
