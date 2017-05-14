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
server_ip = 'localhost'
server_port = '8081'

class tokenizer(View):
	@method_decorator(csrf_exempt)
	def dispatch(self, request, *args, **kwargs):
		return super(tokenizer, self).dispatch(request, *args, **kwargs)

	def parse_json_data(self, request_body):
		json_object = json.loads(request_body)
		return json_object

	def get_string_tokens_from_index_pairs(self, sentence, token_idx_pairs):
		ret_val = []
		for pair in token_idx_pairs:
			ret_val.append(sentence[pair[0]:pair[1]])

		return ret_val

	def generate_index_pairs_from_tokens(self, tokens, sentence):
			'''Given all the tokens in order, the function generates the (start, end) index pair for each token'''

			followup = 0
			l = []
			for t in tokens:
				if t != '':
					idx = sentence.find(t)
					if idx != -1:
						l.append((followup + idx, followup + idx + len(t)))
						sentence = sentence[idx + len(t):]
						followup += idx + len(t)
			return l

	def post(self, request):
		json_obj = self.parse_json_data(request.body)
		server_proxy_address = 'http://' + server_ip + ':' + server_port
		tokenizer_server_proxy = xmlrpclib.ServerProxy(server_proxy_address)


		sentence_pairs = json_obj['sentence_pairs']

		all_tokens = []
		for source_sent, target_sent in sentence_pairs:
			tokens = []
			source_lang = json_obj['source_language'][0:3].upper()
			target_lang = json_obj['target_language'][0:3].upper()
			
			s_t = tokenizer_server_proxy.tokenize(source_sent, source_lang)
			t_t = tokenizer_server_proxy.tokenize(target_sent, target_lang)

			tokens.append(self.generate_index_pairs_from_tokens(s_t, source_sent))
			tokens.append(self.generate_index_pairs_from_tokens(t_t, target_sent))
			all_tokens.append(tokens)

		json_obj['tokens'] = all_tokens
		return JsonResponse(json_obj)