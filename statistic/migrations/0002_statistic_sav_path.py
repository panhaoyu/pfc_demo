# Generated by Django 3.0.1 on 2019-12-23 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statistic', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='statistic',
            name='sav_path',
            field=models.FilePathField(default='', verbose_name='存储文件路径'),
            preserve_default=False,
        ),
    ]
