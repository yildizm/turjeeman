# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-14 16:22
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('storage', '0010_auto_20170514_1621'),
    ]

    operations = [
        migrations.CreateModel(
            name='Storage',
            fields=[
                ('project_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=30)),
                ('source_language', models.CharField(max_length=15)),
                ('target_language', models.CharField(max_length=15)),
                ('timestamp', models.DateField()),
                ('sentence_pairs', django.contrib.postgres.fields.jsonb.JSONField(default=[['', '']])),
                ('tokens', django.contrib.postgres.fields.jsonb.JSONField(default=[])),
                ('mappings', django.contrib.postgres.fields.jsonb.JSONField(default=[[[[[0, 0], [0, 0]], [[0, 0]]]]])),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'storage',
            },
        ),
        migrations.RemoveField(
            model_name='project',
            name='username',
        ),
        migrations.DeleteModel(
            name='Project',
        ),
    ]
