from django.contrib import admin
from .models import Conductor,Pasajero,Administrador

# Register your models here.

admin.site.register(Conductor)
admin.site.register(Pasajero)
admin.site.register(Administrador)