from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('flights/', views.get_flights),
    path('flights/<int:price>/', views.get_flights_price)
]
