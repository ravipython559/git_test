# Generated by Django 2.2.5 on 2019-10-17 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0009_auto_20191010_1924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examslot',
            name='slot_name',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
