from django.urls import path
from . import views
import api

urlpatterns = [
    path('register_order/', views.register_order),
]
