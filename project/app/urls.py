from django.urls import path
from .views import *

urlpatterns = [
    path("", home, name="home"),
    path("contact/", contact, name="contact"),
    path("product/<int:pk>", product, name="product"),
    path("pro_detail/", pro_detail, name="pro_detail"),
    path('show/', show, name="show"),
    path('add_cart/<int:pk>', add_cart, name="add_cart"),
    path('cart/',cart,name='cart'),
    path('remove/<int:pk>', remove, name="remove"),
    path('logout/',logout,name='logout'),


    path('signup/', signup, name="signup"),
    path('signin/', signin, name="signin"),
    path('usersignin/', usersignin, name="usersignin"),
    path('usersignup/', usersignup, name="usersignup"),


    # Admin Part
    path("adminpage/",adminpage,name='adminpage'),
    path('viewuser/',viewuser,name='viewuser'),
    path('update/<int:pk>/', update, name='update'),
    path('delete/<int:pk>/', delete, name="delete"),

]
