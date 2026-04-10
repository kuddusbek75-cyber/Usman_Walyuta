from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/rates/', views.get_rates, name='rates'),
]