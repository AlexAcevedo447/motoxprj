
import json
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
        editable = True
        administrador = True
        
        pasajeros = Pasajero.objects.all()
        conductores = Conductor.objects.all()
        sesion = Sesiones.objects.all()
        
        try:
            current = Sesiones.objects.get(correo = email, contrasena = passw)
        
            if len(current)>0 and current.correo == usr.correo and current.contrasena == usr.contrasena  :
                sesion = Sesiones.objects.all()
            
            elif len(current) == 0:
                Sesiones.objects.create(id=usr.id, nombre=usr.nombre, cedula=usr.cedula, correo=usr.correo, contrasena=usr.contrasena)
                
                
        except Sesiones.DoesNotExist:
            pass
            
        
        
        contexto = {
                    "permisos" : administrador,
                    "pasajeros" : pasajeros,
                    "conductores" : conductores,
                    "editable" : editable,
                    "admiistrador" : sesion
                }
        
        return render(request, "motoxapp/admin/inicio_admin.html", contexto)
    
    except Administrador.DoesNotExist:    
        
        mensaje = "Usuario y contraseña incorrectos"
        return render(request,"motoxapp/errores/error_ingreso.html",mensaje)  
    
    
def inicioAdmin():
    return redirect("motoxapp/admin/inicio_admin.html")

def logOutPas(request):
    return HttpResponse("Saliendo")
    
def guardarPasajero(request):
    
    if request.method == 'POST':
        ident = request.POST['id']
        nombre = request.POST['nombre']
        cedula = request.POST['cedula']
        correo = request.POST['correo']
        contra = request.POST['contrasena']
        
    try:
        Pasajero.objects.create(id = ident, nombre = nombre, cedula = cedula, correo = correo, contrasena = contra)
        
        return  render(request,"motoxapp/admin/inicio_admin.html",adminData())
        
    except Exception:
        mensaje = "Registro no guardado"
        
        return render(request, "motoxapp/admin/inicio_admin.html",mensaje)
    
def guardarConductor(request):
    
    if request.method == 'POST':
        ident = request.POST['id']
        nombre = request.POST['nombre']
        cedula = request.POST['cedula']
        correo = request.POST['correo']
        contra = request.POST['contrasena']
        
    try:
        Conductor.objects.create(id = ident, nombre = nombre, cedula = cedula, correo = correo, contrasena = contra)
        
        return  render(request,"motoxapp/admin/inicio_admin.html",adminData())
        
    except Exception:
        mensaje = "Registro no guardado"
        
        return render(request, "motoxapp/admin/inicio_admin.html",mensaje)
    
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
    
        return  render(request,"motoxapp/admin/inicio_admin.html",adminData())
    except Exception:
    
        return render(request,"motoxapp/admin/inicio_admin.html")
    
def listarPasajero(request, urlRedirect):
    pasajeros = Pasajero.objects.all()
    
    return render(request, urlRedirect, pasajeros)

def listarConductor(request,urlRedirect):
    conductores = Pasajero.objects.all()
    
    return render(request, urlRedirect, conductores)

def listarAmbos(request, urlRedirect):
    listarPasajero(request,urlRedirect)
    listarConductor(request, urlRedirect)
    
def filtrarPasajero(request, id):
    pasajero = list(Pasajero.objects.filter(id = id).values())
    
    return JsonResponse(pasajero,safe=False)

def filtrarConductor(request, id):
    conductor = list(Conductor.objects.filter(id = id).values())
    
    return JsonResponse(conductor,safe=False)
    
def editarConductor(request):
    pass

def editarPasajero(request):
    pass
    

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
        "admiistrador" : sesion
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

def delete(request):
     pass