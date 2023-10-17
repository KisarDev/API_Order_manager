from django.urls import path
from . import views
import api

urlpatterns = [
    path('register_order/', views.register_order_product, name='register_order'),
    path('create_product/', views.create_product, name='create_product'),
]
