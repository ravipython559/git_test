# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2019-10-14 11:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bits_admin', '0049_merge'),
    ]

    operations = [
        migrations.RenameField(
            model_name='candidateselectionarchived',
            old_name='offer_letter',
            new_name='offer_letter_tmp',
        ),
    ]