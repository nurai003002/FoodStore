from django.urls import path, include
from apps.base import views
from apps.secondary.views import about, menu, shop, reservation, cart,details, blog_details, wishlist

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', about, name='about'),
    path('menu/', menu, name='menu'),
    path('shop/', shop, name='shop'),
    path('contacts/', views.contacts, name='contacts'),
    path('reservation', reservation, name='reservation'),
    path('cart/', cart, name='cart' ), 
    path('details/<int:id>/', details, name='details'),
    path('blog_details/<int:id>/', blog_details, name='blog_details'),
    path('wishlist/', wishlist, name='wishlist')
    
]