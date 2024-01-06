from django.urls import path, include
from apps.base import views
from apps.secondary.views import about, menu, shop, reservation, cart,details

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', about, name='about'),
    path('menu/', menu, name='menu'),
    path('shop/', shop, name='shop'),
    path('contacts/', views.contacts, name='contacts'),
    path('reservation', reservation, name='reservation'),
    path('cart/', cart, name='cart' ), 
    path('details', details, name='details'),
    
]