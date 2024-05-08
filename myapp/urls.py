# hotel/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('hotels/', views.hotel_list, name='hotel_list'),
    # Add other URLs if needed
]
