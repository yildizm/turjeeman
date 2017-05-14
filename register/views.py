# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse, HttpResponse
# Create your views here.
class register(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(register, self).dispatch(request, *args, **kwargs)
    def post(self, request):
    	data = json.loads(request.body)
        if User.objects.filter(username=data['username']).exists():
            return HttpResponse("BAD")
        else:
            user = User.objects.create_user(username=data['username'],password=data['password'])
            user.email = data['username']
            user.first_name = data['firstName']
            user.last_name = data['lastName']
            user.is_active=True
            user.save()
            #send_mail('subject', 'msg [include activation link to View here to activate account]', 'from_email', ['to_email'], fail_silently=False)
            return JsonResponse({'response':"OK"})

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