
from django import views
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="inicio"),
    path("conductor", views.loginCond, name="loginCond"),
    path("conductor/validar", views.validarConductor, name="validarConductor"),
    path("conductor/listar", views.listarConductor, name="listarConductor"),
    
    path("conductor/editar", views.editarConductor, name="editarConductor"),
    
    path("pasajero", views.loginPas, name="loginPas"),
    path("pasajero/validar", views.validarPasajero, name="validarPasajero"),
    path("admin/listarPas", views.listarPasajero, name="listarPasajero"),
    
    path("pasajero/editar", views.editarPasajero, name="editarPasajero"),
    
    path("admin", views.loginAdmin, name="loginAdmin"),
    path("admin/inicio", views.validarAdministrador, name="validarAdministrador"),
    path("admin/guardarPas", views.guardarPasajero, name="guardarPasajero"),
    path("admin/guardarCond", views.guardarConductor, name="guardarConductor"),
    path("admin/eliminarCond/<id>", views.eliminarConductor, name="eliminarConductor"),
    path("admin/eliminarPas/<id>", views.eliminarPasajero, name="eliminarPasajero"),
    path("filtrarPas/<id>", views.filtrarPasajero, name="filtrarPasajero"),
    path("filtrarCond/<id>", views.filtrarConductor, name="filtrarConductor"),
]