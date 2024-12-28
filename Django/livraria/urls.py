from django.urls import path
from django.http import HttpResponse
from livraria.views import home, sobre

urlpatterns = [
    path('', home),
    path('sobre/', sobre)
]
