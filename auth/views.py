# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
import json
from SentenceMapper.mapper import Mapper

# Create your views here.
class auth_data(View):
	@method_decorator(csrf_exempt)
	def dispatch(self, request, *args, **kwargs):
		return super(auth_data, self).dispatch(request, *args, **kwargs)

	def get(self,request):
		print request.method
		return JsonResponse({'data_list': [{'name': 'ALİ'}, {'name': 'mustafa'}]})

	def post(self,request):
		mapper = Mapper()
		sent_A = 'It was the best of times'
		tokens_A = ['It', 'was', 'the', 'best', 'of', 'times']
		sent_B = 'Zamanlarin en iyisi idi'
		tokens_B = ['Zamanlarin', 'en', 'iyi', 'si', 'idi']
		auto_map = mapper.auto_map_sentences(sent_A, tokens_A, sent_B, tokens_B)
	
		print '\nAuto mapped index pairs:'
		for k, v in auto_map.items():
			print v
		#print 'Raw Data: "%s"' % request.POST.get('username')
		with open('data.txt', 'w') as outfile:
			print "hebele"
			json.dump(request.body, outfile)
		#return JsonResponse({'data_list': [{'name': 'ALİ'}, {'name': 'mustafa'}]})
		return HttpResponse("OK")
		#print request.POST
		#return JsonResponse({'data_list': [{'name': 'ALİ'}, {'name': 'mustafa'}]})





	
