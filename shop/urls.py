from django.urls import path
from . import views

urlpatterns = [
    path('', views.index , name='ShopHome'),
    path('about/', views.about , name='AboutUs'),
    path('contect/', views.contect, name='ContectUs'),
    path('tracker/', views.tracker, name='Tracker'),
    path('product/<int:my_id>', views.product_view, name='product_view'),
    path('cart/', views.cart, name='product_cart'),
    path('buynow/', views.buynow, name='buy_now')
]