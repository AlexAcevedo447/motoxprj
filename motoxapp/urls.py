
from django import views
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="inicio"),
<<<<<<< HEAD
    path("loginCond", views.loginCond, name="loginCond"),
    path("inicioCond", views.inicioCond, name="inicioCond"),
    path("validarCond", views.validarConductor, name="validarConductor"),
    path("guardarCond", views.guardarConductor, name="guardarConductor"),
    path("editarCond/<id>", views.editarConductor, name="editarConductor"),
    path("formEditarCond/<id>", views.formEditarConductor, name="formEditarCond"),
    path("eliminarCond/<id>", views.eliminarConductor, name="eliminarConductor"),
    path("filtrarCond/<id>", views.filtrarConductores, name="filtrarConductor"),
    path("loginPas", views.loginPas, name="loginPas"),
    path("inicioPas", views.inicioPas, name="inicioPas"),
    path("validarPas", views.validarPasajero, name="validarPasajero"),
    path("guardarPas", views.guardarPasajero, name="guardarPasajero"),
    path("editarPas", views.editarPasajero, name="editarPasajero"),
    path("eliminarPas/<id>", views.eliminarPasajero, name="eliminarPasajero"),
    path("filtrarPas/<id>", views.filtrarPasajeros, name="filtrarPasajero"),
    path("loginAdmin", views.loginAdmin, name="loginAdmin"),
    path("inicioAdmin", views.inicioAdmin, name="inicioAdmin"),
    path("validarAdmin", views.validarAdministrador, name="validarAdministrador"),
=======
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
>>>>>>> 654be4f0520b1e0f19bdc43385b92ceda64e467b
]