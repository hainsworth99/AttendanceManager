# Generated by Django 2.0 on 2019-08-28 04:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('traininggroups', '0002_auto_20190827_2046'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='traininggroup',
            name='generated_at',
        ),
    ]
