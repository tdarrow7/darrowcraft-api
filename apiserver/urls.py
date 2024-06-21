# example/urls.py
from django.urls import path

from apiserver.views import index


urlpatterns = [
    path('', index),
]