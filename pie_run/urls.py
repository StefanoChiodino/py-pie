from django.urls import path

from . import views

app_name = 'pie_run'
urlpatterns = [
    path('', views.index, name='index'),
    path('<uuid:pie_run_id>/', views.pie_run, name='pie_run'),
]
