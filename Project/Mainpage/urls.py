from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # brand-specific pages
    path('acer/', views.acer, name='acer'),
    path('asus/', views.asus, name='asus'),
    path('dell/', views.dell, name='dell'),
    path('hp/', views.hp, name='hp'),
    path('lenovo/', views.lenovo, name='lenovo'),
    path('sony/', views.sony, name='sony'),
]
