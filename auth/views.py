# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

# Create your views here.

def auth_data(request):
    if request.method == 'POST':
	print 'hebele'
        print request.method
        return JsonResponse({'data_list': [{'username': 'deneme'}, {'password': '123456'}]})
    else:
        return HttpResponse('')
