from django.urls import path, include
from apps.base import views
from apps.secondary.views import about, menu, shop

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', about, name='about'),
    path('menu/', menu, name='menu'),
    path('shop/', shop, name='shop'),
]