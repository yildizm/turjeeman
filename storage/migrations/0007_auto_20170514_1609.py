# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-14 16:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0006_auto_20170514_1454'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='id',
        ),
        migrations.AddField(
            model_name='project',
            name='project_id',
            field=models.AutoField(default=0, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
