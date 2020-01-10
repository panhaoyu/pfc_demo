# Generated by Django 3.0.1 on 2019-12-23 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statistic', '0005_auto_20191223_1852'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='max_cycle',
            field=models.IntegerField(default=100000, verbose_name='最多执行的循环数'),
        ),
        migrations.AlterField(
            model_name='project',
            name='cycle_step',
            field=models.IntegerField(default=1000, verbose_name='加载时的步长'),
        ),
    ]