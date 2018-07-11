# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import json, urllib2

# Create your views here.

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

# @csrf_exempt
# #@api_view(['GET'])
# def user_list(request):
#     # TODO: if no token, omit email and lastname
#     if request.method == 'GET':

def index(request):
    return HttpResponse("YES!")

def city_detail(request, city, country = "PH"):
    owurl = "http://api.openweathermap.org/data/2.5/weather?q=%s,%s&appid=7c28321f513df745eed19148f4f6ce55" % (city, country)
    #return HttpResponse(owurl)
    req = urllib2.Request(owurl)
    resp = urllib2.urlopen(req)
    struct = json.loads(resp.read())
    data = json.dumps(struct)
    return HttpResponse(data)