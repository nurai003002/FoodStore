from django.urls import path, include
from apps.base import views

urlpatterns = [
    path('', views.index, name='index'),
    
]