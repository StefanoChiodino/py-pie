from django.conf.urls import url
from . import views

app_name = 'pie_run'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<pie_run_id>[a-zA-Z0-9\-]+?)/$', views.pie_run, name='pie_run'),
]
