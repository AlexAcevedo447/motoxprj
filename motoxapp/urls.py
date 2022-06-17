from django import views
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="inicio"),
    path("conductor", views.loginCond, name="loginCond"),
    path("conductor/validar", views.validarConductor, name="validarConductor"),
    path("conductor/guardar", views.guardarConductor, name="guardarConductor"),
    path("conductor/eliminar/<id>", views.eliminarConductor, name="eliminarConductor"),
    path("pasajero", views.loginPas, name="loginPas"),
    path("pasajero/validar", views.validarPasajero, name="validarPasajero"),
    path("pasajero/guardar", views.guardarPasajero, name="guardarPasajero"),
    path("pasajero/eliminar/<id>", views.eliminarPasajero, name="eliminarPasajero"),
    path("admin", views.loginAdmin, name="loginAdmin"),
    path("admin/inicio", views.validarAdministrador, name="validarAdministrador"),
]