from django.urls import path, include
from apps.base import views
from apps.secondary.views import about, menu, shop, reservation, cart,details, blog_details, wishlist, blogs,add_to_cart, remove_from_cart,add_to_wishlist, remove_from_wishlist

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
    path('wishlist/', wishlist, name='wishlist'),
    path('blogs/',blogs, name='blogs' ),
    path('add_to_cart/<int:food_id>/',add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:cart_item_id>/', remove_from_cart, name='remove_from_cart'),
    path('add_to_wishlist/<int:food_id>/', add_to_wishlist, name='add_to_wishlist'),
    path('remove_from_wishlist/<int:wishlist_item_id>/', remove_from_wishlist, name='remove_from_wishlist'),

    
]