# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from cxgweather.settings import BASE_DIR
import json, os, urllib2

# Create your views here.

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def index(request):
    return HttpResponse("YES!")

@csrf_exempt
def city_detail(request, city, country = "PH"):
    owurl = "http://api.openweathermap.org/data/2.5/weather?q=%s,%s&appid=7c28321f513df745eed19148f4f6ce55&units=metric" % (city, country)
    req = urllib2.Request(owurl)
    resp = urllib2.urlopen(req)
    struct = json.loads(resp.read())
    data = json.dumps(struct)
    return HttpResponse(data)


@csrf_exempt
def cities_list(request):
    #cities_data = open(os.path.join(BASE_DIR, "cities.json"), 'r')
    cities_data = open("C:\_git\cxg\src\cxgweather\cxgweather\cities.json")
    cities_json = json.load(cities_data)
    cities = json.dumps(cities_json)
    cities_data.close
    return HttpResponse(cities)