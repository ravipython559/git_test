# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2021-09-02 04:36
from __future__ import unicode_literals

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('semester_api', '0005_semzestemitransaction_zest_emi_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='semzestemitransaction',
            name='callback_meta',
            field=jsonfield.fields.JSONField(blank=True, null=True),
        ),
    ]