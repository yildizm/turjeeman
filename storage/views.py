# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views import View
from datetime import datetime
from django.shortcuts import render
from storage.models import Project
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.models import User
import json
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
# Create your views here.

# Create your views here.
class storage(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(storage, self).dispatch(request, *args, **kwargs)

    def post(self, request):
        data = json.loads(request.body)
        username = data['username']
        if data['status'] == 'fetch':
            pList = list(Project.objects.filter(username=User.objects.get(username=data['username'])).values())
            return JsonResponse(dict(projects=pList,response='OK'))
        elif data['status'] == 'store':
            print data['username'],data['id'],data['inputText']
            project = Project.objects.get(username=User.objects.get(username=data['username']),project_id=data['id'])
            project.title = data['title']
            print project.title
            project.source_language = data['source_language']
            project.target_language = data['target_language']
            print project.sentence_pairs 
            if project.sentence_pairs == [["",""]]:
                project.sentence_pairs = [[data['inputText'],data['outputText']]]
            else:
                project.sentence_pairs = data['sentence_pairs']
            print project.sentence_pairs
            project.inputText = data['inputText']
            project.outputText = data['outputText']
            project.timestamp = datetime.now()
            #project.sentence_pairs =  data['sentence_pairs']
            #project.tokens =  data['tokens']
            #project.mappings =  data['mappings']
            #project.sentence_pairs = [["It was the best of times, it was the worst of times", "Zamanlarin en iyisi idi, zamanlarin en kotusu idi."], ["It was the age of wisdom.", "Bilgelik cagi idi."]]
            project.save()
            return HttpResponse("OK")
        elif data['status'] == 'create':
            p = Project(username=User.objects.get(username=username),timestamp=datetime.now())
            p.save()
            return JsonResponse({'id':p.project_id,'timestamp':p.timestamp,'response':'OK'})

    def get(self, request):
        username = None
        if request.user.is_authenticated():
            print request.user.username
        data = json.loads(request.body)
        username = data['username']
        print username
    	#p = Project.objects.get(username=User.objects.get(username='ali'))
    	#print p.title,p.source_language,p.target_language,p.timestamp
        #return JsonResponse({'id': p.id, 'title':p.title, 'source_lang': p.source_language, 'target_lang': p.target_language, 'timestamp':p.timestamp,'response':'OK'})
    	return HttpResponse("OK")