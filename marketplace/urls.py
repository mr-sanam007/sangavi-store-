from django.urls import path
from . import views

urlpatterns = [
    path('cart/', views.cart_view, name='cart'),
    path('wishlist/', views.wishlist_view, name='wishlist'),
    path('store/', views.store_view, name='store'),
    path('', views.store_view, name='store'),
] 