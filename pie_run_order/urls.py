from django.conf.urls import url
from . import views

app_name = 'pie_run_order'
urlpatterns = [
    url(r'^details/(?P<pk>[a-zA-Z0-9\-]+?)/$', views.DetailView.as_view(), name='details'),
    url(r'^add/', views.add, name='add'),
]
