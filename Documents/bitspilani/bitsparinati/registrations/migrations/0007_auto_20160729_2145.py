# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-29 16:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registrations', '0006_auto_20160718_1317'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicantionDocumentReason',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'Application Document Rejection Reason',
            },
        ),
        migrations.CreateModel(
            name='ApplicantRejectionReason',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='BitsRejectionReason',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='CandidateSelection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.CharField(max_length=11)),
                ('verified_student_name', models.CharField(max_length=100)),
                ('name_verified_on', models.DateTimeField(auto_now=True)),
                ('name_verified_by', models.CharField(max_length=45)),
                ('selected_rejected_on', models.DateTimeField(blank=True, null=True)),
                ('selection_rejection_comments', models.CharField(blank=True, max_length=45, null=True)),
                ('bits_selection_rejection_by', models.CharField(max_length=45)),
                ('accepted_rejected_by_candidate', models.DateTimeField(blank=True, null=True)),
                ('rejection_by_candidate_comments', models.CharField(blank=True, max_length=50, null=True)),
                ('offer_reject_mail_sent', models.DateTimeField(blank=True, null=True)),
                ('application', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='candidateselection_requests_created_5550', to='registrations.StudentCandidateApplication')),
                ('bits_rejection_reason', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='candidateselection_requests_created_5651', to='registrations.BitsRejectionReason')),
                ('rejection_by_candidate_reason', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='candidateselection_requests_created_5651', to='registrations.ApplicantRejectionReason')),
            ],
        ),
        migrations.AddField(
            model_name='applicationdocument',
            name='accepted_verified_by_bits_flag',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='applicationdocument',
            name='inspected_on',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='modified'),
        ),
        migrations.AddField(
            model_name='applicationdocument',
            name='rejected_by_bits_flag',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='applicationdocument',
            name='reload_flag',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='applicationdocument',
            name='verified_rejected_by',
            field=models.CharField(blank=True, max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='program',
            name='alternative_program_code',
            field=models.CharField(blank=True, max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='program',
            name='organization_name',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='program_fees_admission',
            name='fee_expiry',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='program_fees_admission',
            name='fee_type',
            field=models.CharField(choices=[(None, 'Choose Fee Type'), ('1', 'Admission Fee'), ('2', 'Application Fee')], default=1, max_length=16),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='applicationdocument',
            name='last_uploaded_on',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='modified'),
        ),
        migrations.AddField(
            model_name='applicationdocument',
            name='rejection_reason',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='applicationdocument_requests_created_5859', to='registrations.ApplicantionDocumentReason'),
        ),
    ]
