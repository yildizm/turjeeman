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
            #p = Project.objects.get(username=User.objects.get(username=username))
            pList= list(Project.objects.filter(username=User.objects.get(username=username)))
            for p in pList:
                print("title: "+p.title)
            return JsonResponse({'id': pList[0].id, 'title':pList[0].title, 'source_lang': pList[0].source_language, 'target_lang': pList[0].target_language, 'timestamp':pList[0].timestamp,'response':'OK'})
        elif data['status'] == 'store':
            project = Project.objects.get(username=User.objects.get(username=username),id=data['id'])
            project.title = data['title']
            project.source_language = data['source_language']
            project.target_language = data['target_language']
            project.timestamp = datetime.now()
            project.save()
            return HttpResponse("OK")
        else:
            p = Project(username=User.objects.get(username=username),timestamp=datetime.now())
            p.save()
            return JsonResponse({'id':p.id,'timestamp':p.timestamp,'response':'OK'})

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