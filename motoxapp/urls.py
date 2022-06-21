from django import views
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="inicio"),
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
]