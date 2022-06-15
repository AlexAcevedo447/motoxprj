
from django.shortcuts import render
from django.http.response import JsonResponse, HttpResponse
from django.views import View
from .models import Conductor,Pasajero,Administrador

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
        
        conductores = Conductor.objects.all()
        
        contexto = {
            "conductores": conductores,
            "pasajero" : usr
        }
        
        return render(request, "motoxapp/pasajero/inicio_pas.html", contexto)
    
    except Pasajero.DoesNotExist:    
        
        mensaje = "Usuario y contraseña incorrectos"
        return render(request,"motoxapp/errores/error_ingreso.html")
    
def logOutPas(request):
    return HttpResponse("Saliendo")
    
def post(request):
    pass
    
def put(request):
     pass

def delete(request):
     pass