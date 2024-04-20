from django.urls import path,include

from .views import *

urlpatterns = [

    path('', products, name='products'),
    path('home/', home, name='home'),
    path('product/<int:pk>/', product_detail, name='product_detail'),
    path('account/',include('django.contrib.auth.urls')),
    path('logout/', logout, name='loGout'),
]
