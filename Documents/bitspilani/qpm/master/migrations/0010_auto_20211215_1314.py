# Generated by Django 3.2 on 2021-12-15 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0009_auto_20211215_1308'),
    ]

    operations = [
        migrations.AddField(
            model_name='batch',
            name='sem_number',
            field=models.CharField(choices=[(None, 'Choose Semester Number'), ('1', '1'), ('2', '2')], max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='batch',
            name='year',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='examtype',
            name='evaluation_type',
            field=models.CharField(choices=[(None, 'Choose Evaluation Type'), ('EC2', 'EC2'), ('EC3', 'EC3'), ('CERTIFICATION', 'CERTIFICATION')], max_length=14, null=True),
        ),
        migrations.AlterField(
            model_name='examtype',
            name='exam_type',
            field=models.CharField(max_length=45),
        ),
        migrations.AlterUniqueTogether(
            name='examtype',
            unique_together={('exam_type', 'evaluation_type')},
        ),
    ]