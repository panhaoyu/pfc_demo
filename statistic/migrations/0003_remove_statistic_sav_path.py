# Generated by Django 3.0.1 on 2019-12-23 07:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('statistic', '0002_statistic_sav_path'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='statistic',
            name='sav_path',
        ),
    ]
