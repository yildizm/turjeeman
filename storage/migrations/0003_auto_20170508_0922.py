# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-08 09:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0002_auto_20170507_2317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='source_language',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='project',
            name='target_language',
            field=models.CharField(max_length=15),
        ),
    ]