
from asyncio.windows_events import NULL
from contextlib import nullcontext
from django.shortcuts import render,redirect
from django.http.response import JsonResponse, HttpResponse
from django.views import View
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

def logOutPas(request):
    return HttpResponse("Saliendo")

def filtrarConductores(request,id):
    
    conductores = list(Conductor.objects.filter(id = id).values())
    
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
    
def editarPasajero(request):
    pass

def editarConductor(request):
    pass
    
def eliminarPasajero(request, id):
    pasajero = Pasajero.objects.get(id = id)
    
    try:
        pasajero.delete()
    
        return render(request,"motoxapp/admin/inicio_admin.html",adminData())
    except Exception:
    
        return render(request,"motoxapp/admin/inicio_admin.html",adminData())

    
    
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
