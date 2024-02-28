from django.urls import path
from .views import *

urlpatterns = [
    path("", home, name="home"),
    path("contact/", contact, name="contact"),
    path("product/<int:pk>", product, name="product"),
    path("pro_detail/", pro_detail, name="pro_detail"),
    path('show/', show, name="show"),
    path('add_cart/<int:pk>', add_cart, name="add_cart"),
    path("adminpage/",adminpage,name='adminpage'),
    path('cart/',cart,name='cart'),
]
