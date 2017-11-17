from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^pie-run/(?P<id>[a-zA-Z0-9\-]+?)/$', views.pie_run, name='pie_run'),
    url(r'^', views.index, name='index'),
]