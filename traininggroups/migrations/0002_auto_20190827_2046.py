# Generated by Django 2.0 on 2019-08-28 03:46

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('traininggroups', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='traininggroup',
            name='group_members_student_id',
        ),
        migrations.AddField(
            model_name='traininggroup',
            name='group_members',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=250), null=True, size=None),
        ),
    ]