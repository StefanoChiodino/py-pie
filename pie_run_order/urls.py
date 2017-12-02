from django.urls import path

from . import views

app_name = 'pie_run_order'
urlpatterns = [
    path('details/<uuid:pk>/', views.DetailView.as_view(), name='details'),
    path('add/', views.add, name='add'),
]
