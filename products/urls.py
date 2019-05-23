from django.urls import path
from . import views

urlpatterns = [
    path('<int:int>/', views.product, name='product'),
]