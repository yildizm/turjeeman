# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views import View

# Create your views here.
server_ip = '139.179.103.66'
server_port = '8080'

class mapper(View):
    def post(self, request):
        json_obj = parse_json_data(request.body)
		sentence_pairs = json_obj['sentence_pairs']
		tokens = json_obj['tokens']

		server_proxy_address = 'http://' + server_ip + ':' + server_port
		mapper_server_proxy = xmlrpclib.ServerProxy(server_proxy_address)

		mappings = []
		for i, (source_tokens, target_tokens) in enumerate(tokens):
			source_tokens.sort(key=lambda pair: pair[0])
			target_tokens.sort(key=lambda pair: pair[0])

			s_str_tokens = get_string_tokens_from_index_pairs(sentence_pairs[i][0], source_tokens)
			t_str_tokens = get_string_tokens_from_index_pairs(sentence_pairs[i][1], target_tokens)

			hyperedge_dict = mapper_server_proxy.auto_map_sentences(sentence_pairs[i][0], s_str_tokens, sentence_pairs[i][1], t_str_tokens, json_obj['source_language'], json_obj['target_language'])

			sent_map = []
			for k, v in hyperedge_dict.items():
				single_map = [v[0], v[1]]
				sent_map.append(single_map)

			mappings.append(sent_map)

		json_obj['mappings'] = mappings
        return JsonResponse(json_obj)

	def parse_json_data(request_body):
		json_object = json.loads(request_body)
		return json_object

	def generate_graph_id(lang_A, lang_B):
			if lang_A < lang_B:
				return lang_A + '-' + lang_B
			else:
				return lang_B + '-' + lang_A

	def get_string_tokens_from_index_pairs(sentence, token_idx_pairs):
		ret_val = []
		for pair in token_idx_pairs:
			ret_val.append(sentence[pair[0]:pair[1]])

		return ret_val


