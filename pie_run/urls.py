from django.conf.urls import url

from . import views

app_name = 'pie_run'
urlpatterns = [
    url('', views.index, name='index'),
    url('<uuid:pie_run_id>/', views.pie_run, name='pie_run'),
]
