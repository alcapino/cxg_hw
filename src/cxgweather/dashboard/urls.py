from django.conf.urls import url
from dashboard import views

urlpatterns = [
    url(r'^weather/$', views.index),
    url(r'^weather/(?P<city>[\w]+)$', views.city_detail),
]