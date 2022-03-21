from django.urls import path
from . import views

urlpatterns = [
    #Index Page
    path('', views.index, name='index'),
]
