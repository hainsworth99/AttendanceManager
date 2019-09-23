# Generated by Django 2.0 on 2019-08-28 03:35

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TrainingGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('group_members_student_id', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), size=None)),
                ('generated_at', models.DateTimeField()),
            ],
        ),
    ]