# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views import View
import xmlrpclib, json
from SimpleXMLRPCServer import SimpleXMLRPCServer

# Create your views here.
server_ip = '139.179.103.66'
server_port = '8082'

class sentence(View):
	@method_decorator(csrf_exempt)
	def dispatch(self, request, *args, **kwargs):
		return super(sentence, self).dispatch(request, *args, **kwargs)

	def parse_json_data(self, request_body):
    json_object = json.loads(request_body)
    return json_object

    def post(self, request):
    	json_obj = self.parse_json_data(request.body)
		sentence_pairs = json_obj['sentence_pairs']

		server_proxy_address = 'http://' + server_ip + ':' + server_port
		sentencer_server_proxy = xmlrpclib.ServerProxy(server_proxy_address)

		source_text = ''
		target_text = ''

		for s, t in sentence_pairs:
		    source_text = source_text + s
		    target_text = target_text + t

		source_lang = json_obj['source_language']
		target_lang = json_obj['target_language']

		json_obj['sentence_pairs'] = sentencer_server_proxy.get_sentence_to_sentence_mapping(source_text, target_text, source_lang, target_lang)[0]
		return JsonResponse(json_obj)