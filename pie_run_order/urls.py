from django.conf.urls import url

from . import views

app_name = 'pie_run_order'
urlpatterns = [
    url('details/<uuid:pk>/', views.DetailView.as_view(), name='details'),
    url('add/', views.add, name='add'),
]
