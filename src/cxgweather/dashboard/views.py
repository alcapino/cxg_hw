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

@csrf_exempt
def index(request):
    return HttpResponse("YES!")

@csrf_exempt
def city_detail(request, city, country = "PH"):
    owurl = "http://api.openweathermap.org/data/2.5/weather?q=%s,%s&appid=7c28321f513df745eed19148f4f6ce55" % (city, country)
    #return HttpResponse(owurl)
    req = urllib2.Request(owurl)
    resp = urllib2.urlopen(req)
    struct = json.loads(resp.read())
    data = json.dumps(struct)
    return HttpResponse(data)


@csrf_exempt
def cities_list(request):
    response = "[ { \"id\": 1701668, \"name\": \"Manila\" },{ \"id\": 7521309, \"name\": \"Davao\" },{ \"id\": 1721080, \"name\": \"Cagayan de Oro\" },{ \"id\": 1695848, \"name\": \"Angeles\" },{ \"id\": 1698829, \"name\": \"Naga\" },{ \"id\": 1729564, \"name\": \"Bacolod\" },{ \"id\": 1706889, \"name\": \"Legazpi\" },{ \"id\": 1728930, \"name\": \"Baguio\" },{ \"id\": 1726280, \"name\": \"Batangas\" }]"
    #response = "{ id: 1701668, name: 'Manila' }";
    data = json.dumps(response)
    return HttpResponse(data)