# Generated by Django 2.2.5 on 2019-09-24 10:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0006_auto_20190912_1830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseexamshedule',
            name='batch',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='courseexamshedule_batch', to='master.Batch'),
        ),
        migrations.AlterField(
            model_name='courseexamshedule',
            name='semester',
            field=models.ForeignKey(blank=True, help_text='Only Semesters With Active Exam Entries Are Allowed', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='courseexamshedule_sem', to='master.Semester'),
        ),
    ]