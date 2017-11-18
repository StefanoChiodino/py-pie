from django.conf.urls import url
from . import views

app_name = 'pie_run_order'
urlpatterns = [
    url(r'^details/(?P<pie_run_order_id>[a-zA-Z0-9\-]+?)/$', views.details, name='details'),
    url(r'^add/', views.add, name='add'),
]
