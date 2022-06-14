from django import views
from django.urls import path
from . import views

urlpatterns = [
    path("/", views.index, name="inicio"),
    path("/conductor", views.loginCond, name="loginCond"),
    path("/pasajero", views.loginPas, name="loginPas"),
    path("/pasajero/validar", views.validarPasajero, name="validarPasajero"),
    path("/manager", views.loginAdmin, name="loginAdmin"),
    
]