"""Production App - URLs"""
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name=''),
]