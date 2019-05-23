from django.urls import path

from . import views

urlpatterns = [
    path('<str:str>/', views.search, name='search'),
]