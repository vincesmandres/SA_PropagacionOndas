from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('simulate/', views.simulate_wave, name='simulate_wave'),
]
