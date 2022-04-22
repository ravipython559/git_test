# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-08-04 07:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registrations', '0037_candidateselection_bits_rejection_reason'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicantExceptions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applicant_email', models.EmailField(max_length=254, verbose_name='Applicant email ID / user ID')),
                ('work_ex_waiver', models.BooleanField(default=False, verbose_name='Work Experience waiver required?')),
                ('employment_waiver', models.BooleanField(default=False, verbose_name='Employment waiver required (candidate can be unemployed while applying)?')),
                ('mentor_waiver', models.BooleanField(default=False, verbose_name='Mentor details not required to be provided?')),
                ('offer_letter', models.CharField(blank=True, choices=[(None, 'Choose'), ('offer_pdf/oracle.html', 'oracle'), ('offer_pdf/non-specific-sem2.html', 'Non Specific 2016 2nd Sem'), ('offer_pdf/Specific-program-template.html', 'Specific-program template'), ('offer_pdf/wipro.html', 'Wipro Offer letter'), ('offer_pdf/wipro_sim.html', 'Wipro - SIM'), ('offer_pdf/wipro_wims.html', 'Wipro - WIMS'), ('offer_pdf/wipro_wase.html', 'Wipro - WASE')], max_length=100, null=True, verbose_name='Choose custom offer letter template, if applicable')),
                ('hr_contact_waiver', models.BooleanField(default=False, verbose_name='HR contact details not required to be provided?')),
                ('created_on_datetime', models.DateTimeField(auto_now_add=True)),
                ('org', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='applicantexceptions_coll_org', to='registrations.CollaboratingOrganization', verbose_name='Choose organization')),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applicantexceptions_pg', to='registrations.Program', verbose_name='Choose Program')),
            ],
            options={
                'ordering': ['applicant_email'],
                'verbose_name': 'Applicant Exception',
            },
        ),
        migrations.AlterUniqueTogether(
            name='applicantexceptions',
            unique_together=set([('applicant_email', 'program')]),
        ),
    ]