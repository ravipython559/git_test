# Generated by Django 2.2.7 on 2020-10-08 13:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0025_onlineexamattendance'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExamVenueLock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.CharField(max_length=12)),
                ('lock_flag', models.BooleanField(default=1)),
                ('exam_venue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='examvenuelock_ev', to='master.ExamVenue', verbose_name='Exam Venue Name')),
                ('semester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='examvenuelock_sem', to='master.Semester', verbose_name='Semester Name')),
            ],
        ),
    ]
