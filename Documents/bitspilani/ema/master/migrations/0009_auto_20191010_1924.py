# Generated by Django 2.2.5 on 2019-10-10 13:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0008_auto_20190927_1317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currentexam',
            name='batch',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='currentexam_batch', to='master.Batch'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='currentexam',
            name='semester',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='currentexam_sem', to='master.Semester'),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='hallticket',
            unique_together=set(),
        ),
    ]
