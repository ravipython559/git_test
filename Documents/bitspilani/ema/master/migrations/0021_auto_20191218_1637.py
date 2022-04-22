# Generated by Django 2.2.7 on 2019-12-18 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0020_examvenueslotmap_student_count_limit'),
    ]

    operations = [
        migrations.AddField(
            model_name='examvenueslotmap',
            name='course_exam_schedule',
            field=models.ManyToManyField(blank=True, to='master.CourseExamShedule'),
        ),
        migrations.AlterField(
            model_name='examvenue',
            name='student_count_limit',
            field=models.PositiveIntegerField(verbose_name='Seating Limit'),
        ),
        migrations.AlterField(
            model_name='examvenueslotmap',
            name='student_count_limit',
            field=models.PositiveIntegerField(verbose_name='Student Count Limit'),
        ),
    ]