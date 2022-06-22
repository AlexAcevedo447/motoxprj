

from django.shortcuts import render
import json
from django.http.response import JsonResponse, HttpResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .models import Conductor,Pasajero,Administrador,Sesiones

# Create your views here.

def index(request):
    return render(request,"motoxapp/index.html")

def loginCond(request):
    return render(request,"motoxapp/conductor/login_cond.html")

def loginAdmin(request):
    return render(request,"motoxapp/admin/login_admin.html")

def loginPas(request):
    return render(request,"motoxapp/pasajero/login_pas.html")

def validarPasajero(request):
    
    if request.method == 'POST':
        email = request.POST['email']
        passw = request.POST['contra']
        
        print(f"Usuario = {email}, Contraseña = {passw}") 
    
    try:
        
        usr = Pasajero.objects.get(correo = email, contrasena = passw)
        editable =False
        administrador = False
        
        conductores = Conductor.objects.all()
        
        contexto = {
            "administrador" : administrador,
            "conductores": conductores,
            "pasajero" : usr,
            "editable" : editable
        }
        
        return render(request, "motoxapp/pasajero/inicio_pas.html", contexto)
    
    except Pasajero.DoesNotExist:    
        
        mensaje = "Usuario y contraseña incorrectos"
        return render(request,"motoxapp/errores/error_ingreso.html")
    
    
def validarConductor(request):
    
    if request.method == 'POST':
        email = request.POST['email']
        passw = request.POST['contra']
        
        print(f"Usuario = {email}, Contraseña = {passw}") 
    
    try:
        
        usr = Conductor.objects.get(correo = email, contrasena = passw)
        editable = False
        administrador = False
        
        pasajeros = Pasajero.objects.all()
        
        contexto = {
            "administrador" : administrador,
            "pasajeros": pasajeros,
            "conductor" : usr,
            "editable" : editable
        }
        
        return render(request, "motoxapp/conductor/inicio_cond.html", contexto)
    
    except Conductor.DoesNotExist:    
        
        mensaje = "Usuario y contraseña incorrectos"
        return render(request,"motoxapp/errores/error_ingreso.html")
    

def validarAdministrador(request):
    
    if request.method == 'POST':
        email = request.POST['email']
        passw = request.POST['contra']
        
        print(f"Usuario = {email}, Contraseña = {passw}") 
    
    try:
        
        usr = Administrador.objects.get(correo = email, contrasena = passw)
        
        try:
        
            try:
                sesion = Sesiones.objects.all()
            
            except Sesiones.DoesNotExist:
                sesion=Sesiones.objects.create(id=usr.id, nombre=usr.nombre, cedula=usr.cedula, correo=usr.correo, contrasena=usr.contrasena)
               
            
        except Administrador.DoesNotExist:
            pass
            
        return inicioAdmin(request)
        
    except Administrador.DoesNotExist:    
        
        mensaje = "Usuario y contraseña incorrectos"
        return render(request,"motoxapp/errores/error_ingreso.html",mensaje)  
    
    
def inicioAdmin(request):
    return render(request,"motoxapp/admin/inicio_admin.html",adminData())

def inicioCond(request):
    return render(request,"motoxapp/conductor/inicio_cond.html",condData())

def inicioPas(request):
    return render(request,"motoxapp/pasajero/inicio_pas.html",pasData())

def logOutPas(request,id):
    return HttpResponse("Saliendo")

def formEditarConductor(request,id):
    
    conductor = filtrarConductores(id)
    
    return render(request, "motoxapp/admin/editarCond.html", {"datos": conductor})

def filtrarConductores(id):
    
    conductores = Conductor.objects.get(id = id)
    
    return conductores

def filtrarPasajeros(id):
    
    pasajeros = Pasajero.objects.get(id = id)
    
    return pasajeros
    
def guardarPasajero(request):
    ident = request.POST['id']
    nombre = request.POST['nombre']
    cedula = request.POST['cedula']
    correo = request.POST['correo']
    contra = request.POST['contrasena']
        
    Pasajero.objects.create(id = ident, nombre = nombre, cedula = cedula, correo = correo, contrasena = contra)
        
    return inicioAdmin(request)
    
def guardarConductor(request):
    ident = request.POST['id']
    nombre = request.POST['nombre']
    cedula = request.POST['cedula']
    correo = request.POST['correo']
    contra = request.POST['contrasena']
        
    try:
        Conductor.objects.create(id = ident, nombre = nombre, cedula = cedula, correo = correo, contrasena = contra)
        sesion= Sesiones.objects.all()
        
        return inicioAdmin(request)
        
    except :
        mensaje = "Registro no guardado"
        
        return render(request, "motoxapp/errores/error_consulta.html",{"mensaje":mensaje})
    
@method_decorator(csrf_exempt)
def dispatch(self, request, *args, **kwargs):
    
    return editarPasajero().dispatch(request, *args, **kwargs)
    
def editarPasajero(request):
    pass

@method_decorator(csrf_exempt)
def dispatch(self, request, *args, **kwargs):
    
    return editarConductor().dispatch(request, *args, **kwargs)

def editarConductor(request):
    
    ide= request.POST.get('id',False)
    name= request.POST.get('nombre',False)
    NIT= request.POST.get('cedula',False)
    email= request.POST.get('correo',False)
    passw= request.POST.get('contrasena',False)
    
    cond = Conductor.objects.get(id= ide)
    
    cond.nombre = name
    cond.cedula = NIT
    cond.correo = email
    cond.contrasena = passw
    
    cond.save()
    
    
    
    return inicioAdmin(request)
    
def eliminarPasajero(request, id):
    pasajero = Pasajero.objects.get(id = id)
    
    try:
        pasajero.delete()
    
        return  render(request,"motoxapp/admin/inicio_admin.html",adminData())
    except Exception:
    
        return render(request,"motoxapp/admin/inicio_admin.html")

    
    
def eliminarConductor(request, id):
    conductor =Conductor.objects.get(id = id)
    
    try:
        conductor.delete()
    
        return inicioAdmin(request)
    except Exception:
        mensaje = "Registro no se pudo borrar"
    
        return render(request,"motoxapp/errores/error_consulta.html",mensaje)

def adminData():
    editable = True
    administrador = True
        
    pasajeros = Pasajero.objects.all()
    conductores = Conductor.objects.all()
        
    sesion = Sesiones.objects.all()
        
        
    contexto = {
        "permisos" : administrador,
        "pasajeros" : pasajeros,
        "conductores" : conductores,
        "editable" : editable,
        "administrador" : sesion
    }
    
    return contexto

def pasData():
    usr = Sesiones.objects.all()
    editable =False
    administrador = False
        
    conductores = Conductor.objects.all()
        
    contexto = {
        "administrador" : administrador,
        "conductores": conductores,
        "pasajero" : usr,
        "editable" : editable
    }
    return contexto

def condData():
    usr = Sesiones.objects.all()
    editable = False
    administrador = False
        
    pasajeros = Pasajero.objects.all()
        
    contexto = {
        "administrador" : administrador,
        "pasajeros": pasajeros,
        "conductor" : usr,
        "editable" : editable
    }
    
    return contexto
