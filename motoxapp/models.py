from django.db import models

# Create your models here.

class Conductor(models.Model):
    id = models.IntegerField(primary_key=True,max_length=11)
    nombre = models.CharField(max_length=148)
    cedula = models.CharField(max_length=148)
    correo = models.EmailField(max_length=148)
    contrasena = models.CharField(max_length=148)
    
    
class Pasajero(models.Model):
    id = models.IntegerField(primary_key=True,max_length=11)
    nombre = models.CharField(max_length=148)
    cedula = models.CharField(max_length=148)
    correo = models.EmailField(max_length=148)
    contrasena = models.CharField(max_length=148)
    
class Administrador(models.Model):
    id = models.IntegerField(primary_key=True,max_length=11)
    nombre = models.CharField(max_length=148)
    cedula = models.CharField(max_length=148)
    correo = models.EmailField(max_length=148)
    contrasena = models.CharField(max_length=148)
    
    
class Sesiones(models.Model):
    id = models.IntegerField(primary_key=True,max_length=11)
    nombre = models.CharField(max_length=148)
    cedula = models.CharField(max_length=148)
    correo = models.EmailField(max_length=148)
    contrasena = models.CharField(max_length=148)