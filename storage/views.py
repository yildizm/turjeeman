# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views import View
from datetime import datetime
from django.shortcuts import render
from storage.models import Project
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.models import User
# Create your views here.

# Create your views here.
class storage(View):
    def post(self, request):
    	user = User.objects.get(username='ali')
    	p = Project(title='A Tale of Two Cities', source_language='EN', target_language='TR',timestamp=datetime.now(),username=user)
    	p.save()
        all_entries = Project.objects.all()
        print all_entries
        return HttpResponse('result')
    def get(self, request):
    	p = Project.objects.get(username=User.objects.get(username='ali'))
    	print p.title,p.source_language,p.target_language,p.timestamp
    	return HttpResponse(p)