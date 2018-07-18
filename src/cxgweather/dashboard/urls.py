from django.conf.urls import url
from dashboard import views

urlpatterns = [
    url(r'^city/$', views.cities_list),
    url(r'^weather/$', views.index),
    url(r'^weather/(?P<city>[\w\s]+)/$', views.city_detail),
]