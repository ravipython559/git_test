# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2019-06-11 13:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registrations', '0108_candidateselection_offer_letter'),
        ('bits_rest', '0023_auto_20190604_1909'),
    ]

    operations = [
        migrations.AddField(
            model_name='inboundcall',
            name='application',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='inboundcall_application', to='registrations.StudentCandidateApplication'),
        ),
        migrations.AddField(
            model_name='outboundcall',
            name='application',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='outboundcall_application', to='registrations.StudentCandidateApplication'),
        ),
    ]
