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
server_port = '8080'

class mapper(View):
	@method_decorator(csrf_exempt)
	def dispatch(self, request, *args, **kwargs):
		return super(mapper, self).dispatch(request, *args, **kwargs)

	def parse_json_data(self,request_body):
		json_object = json.loads(request_body)
		return json_object

	def generate_graph_id(self,lang_A, lang_B):
			if lang_A < lang_B:
				return lang_A + '-' + lang_B
			else:
				return lang_B + '-' + lang_A

	def get_string_tokens_from_index_pairs(self,sentence, token_idx_pairs):
		ret_val = []
		for pair in token_idx_pairs:
			ret_val.append(sentence[pair[0]:pair[1]])

		return ret_val

	def post(self, request):
		json_obj = self.parse_json_data(request.body)
		sentence_pairs = json_obj['sentence_pairs']
		mappings = json_obj['mappings']
		graph_id = self.generate_graph_id(json_obj['source_language'], json_obj['target_language'])

		server_proxy_address = 'http://' + server_ip + ':' + server_port
		mapper_server_proxy = xmlrpclib.ServerProxy(server_proxy_address)

		source_tokens = []
		target_tokens = []
		for i, sent in enumerate(mappings):
			s_idx_pair = []
			t_idx_pair = []
			for s, t in sent:
				s_idx_pair.extend(s)
				t_idx_pair.extend(t)

			source_tokens.extend(get_string_tokens_from_index_pairs(sentence_pairs[i][0], s_idx_pair))
			target_tokens.extend(get_string_tokens_from_index_pairs(sentence_pairs[i][1], t_idx_pair))

		mapper_server_proxy.add_token(source_tokens, json_obj['source_language'], graph_id)
		mapper_server_proxy.add_token(target_tokens, json_obj['target_language'], graph_id)

		for i, (source_sent, target_sent) in enumerate(sentence_pairs):
			for m in mappings[i]:
				s = self.get_string_tokens_from_index_pairs(source_sent, m[0])
				t = self.get_string_tokens_from_index_pairs(target_sent, m[1])
				mapper_server_proxy.add_hyperedge(s, t, graph_id)

		# mapper_server_proxy.save_graph_model('ENG-TR')
		return HttpResponse("OK")
