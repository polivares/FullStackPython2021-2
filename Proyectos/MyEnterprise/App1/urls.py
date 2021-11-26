from django.urls import path
from App1 import views

urlpatterns = [
    path('', views.index),
    path('mensaje/', views.index),
    path('solicitudes/', views.solicitudes),
    path('form/', views.form),
]