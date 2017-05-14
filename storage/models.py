# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.contrib.postgres.fields import JSONField

# Create your models here.

class Project(models.Model):
	project_id = models.AutoField(primary_key=True)
	title = models.CharField(max_length=30)
	source_language = models.CharField(max_length=15)
	target_language = models.CharField(max_length=15)
	timestamp = models.DateField()
	username = models.ForeignKey(User, on_delete=models.CASCADE)
	sentence_pairs = JSONField(default=[["",""]])
	tokens = JSONField(default=[])
	mappings = JSONField(default=[[[[[0,0],[0,0]],[[0,0]]]]])
	inputText = models.TextField(default='')
	outputText = models.TextField(default='')
	def __str__(self):              # __unicode__ on Python 2
		return self.title

	class Meta:
		db_table = 'project'
