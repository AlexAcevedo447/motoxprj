from django.shortcuts import render
from django.http.response import JsonResponse, HttpResponse
from django.views import View
from .models import Conductor

# Create your views here.

def index(request):
    return render(request,"motoxapp/index.html")

def loginCond(request):
    return render(request,"motoxapp/conductor/login_cond.html")

def loginAdmin(request):
    return render(request,"motoxapp/admin/login_admin.html")

def loginPas(request):
    return render(request,"motoxapp/pasajero/login_pas.html")
    
def post(request):
    pass
    
def put(request):
     pass

def delete(request):
     pass