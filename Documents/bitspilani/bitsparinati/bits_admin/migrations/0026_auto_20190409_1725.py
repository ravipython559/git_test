# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2019-04-09 11:55
from __future__ import unicode_literals

import bits_admin.models
from django.db import migrations, models
import django.db.models.deletion
import easy_thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
        ('registrations', '0103_auto_20190409_1725'),
        ('bits_admin', '0025_auto_20190215_1843'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProgramArchived',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('program_code', models.CharField(max_length=6)),
                ('program_name', models.CharField(max_length=60)),
                ('form_title', models.CharField(max_length=200)),
                ('alternative_program_code', models.CharField(blank=True, max_length=45, null=True)),
                ('program_type', models.CharField(max_length=30)),
                ('application_pdf_template', models.CharField(blank=True, max_length=60, null=True)),
                ('offer_letter_template', models.CharField(blank=True, max_length=60, null=True)),
                ('collaborating_organization', models.CharField(blank=True, max_length=200, null=True)),
                ('org_logo_image', easy_thumbnails.fields.ThumbnailerImageField(blank=True, null=True, upload_to=bits_admin.models.document_upload_page_path)),
                ('document_upload_page_path', models.CharField(blank=True, max_length=100, null=True)),
                ('active_for_applicaton_flag', models.BooleanField(default=False)),
                ('show_on_page_flag', models.BooleanField(default=False)),
                ('serial_number_on_page', models.PositiveIntegerField()),
                ('show_to_fee_wvr_appl_flag', models.BooleanField(default=False, verbose_name='Show Program to Applicants with fee waivers in other Programs')),
                ('work_exp_check_req', models.BooleanField(default=True, verbose_name='Work Experience Check Required')),
                ('mentor_id_req', models.BooleanField(default=True, verbose_name='Mentor Consent Required')),
                ('min_work_exp_in_months', models.PositiveIntegerField(blank=True, null=True, verbose_name='Minimum Work Experience in Months')),
                ('hr_cont_req', models.BooleanField(default=True, verbose_name='HR Contact Required')),
                ('is_zest_emi_enable', models.BooleanField(default=False)),
                ('enable_pre_selection_flag', models.BooleanField(default=False)),
                ('available_in_cities', models.ManyToManyField(to='registrations.Location')),
            ],
            options={
                'ordering': ['serial_number_on_page'],
            },
        ),
        migrations.CreateModel(
            name='ZestProgramMapArchived',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('merchant_name', models.CharField(max_length=45)),
                ('client_id', models.TextField(verbose_name='Merchant ID')),
                ('client_secret', models.TextField(verbose_name='Merchant Password')),
            ],
        ),
        migrations.AddField(
            model_name='programarchived',
            name='zest',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='programarchived_zest', to='bits_admin.ZestProgramMapArchived'),
        ),
    ]
