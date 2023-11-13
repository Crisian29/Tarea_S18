from django.shortcuts import render
from django.shortcuts import render
from .models import Empleado
# Create your views here.
from django.shortcuts import render
from .models import MiModelo  # Asegúrate de importar tus modelos

def index(request):
    # Recupera todos los objetos de MiModelo desde la base de datos
    objetos = MiModelo.objects.all()

    # Pasa los objetos a la plantilla para su visualización
    return render(request, 'CMIAPP/index.html', {'objetos': objetos})

# CMIAPP/views.py

def lista_empleados(request):
    empleados = Empleado.objects.all()
    return render(request, 'CMIAPP/index.html', {'empleados': empleados})
