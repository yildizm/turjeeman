# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.views import View
from django.contrib.auth import authenticate

import json
import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from SentenceMapper.mapper import Mapper
from SentenceMapper import hypergraph
sys.modules['hypergraph'] = hypergraph

# Create your views here.
class auth(View):
	@method_decorator(csrf_exempt)
	def dispatch(self, request, *args, **kwargs):
		return super(auth, self).dispatch(request, *args, **kwargs)

	def get(self,request):
		print request.method
		return JsonResponse({'data_list': [{'name': 'ALi'}, {'name': 'mustafa'}]})

	def post(self,request):
		#print 'Raw Data: "%s"' % request.body
		#with open('data.txt', 'w') as outfile:
		#	json.dump(request.body, outfile)
		data = json.loads(request.body)
		username = data['username']
		password = data['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			return JsonResponse({'username':username, 'name': user.first_name, 'surname': user.last_name, 'response':'OK'})
		    # A backend authenticated the credentials
		else:
			return JsonResponse({'name': '', 'surname': '', 'response':'BAD'})
			# No backend authenticated the credentials
			#return JsonResponse({'data_list': [{'name': 'ALİ'}, {'name': 'mustafa'}]})





	
