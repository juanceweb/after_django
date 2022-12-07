from django.shortcuts import render
from django.http import HttpResponse
from .models import Familiar

# Create your views here.
def inicio(request):
    return HttpResponse("Hola desde Django cambiado")


def familiar(request):
    familiar1 = Familiar(nombre="Jose", edad=60, anio_nacimiento="1999-10-30")
    familiar1.save()
    familiar2 = Familiar(nombre="Carlos", edad=20, anio_nacimiento="2002-11-01")
    familiar2.save()
    familiar3 = Familiar(nombre="Alicia", edad=10, anio_nacimiento="2012-05-25")
    familiar3.save()
    return render(
        request,
        "familiares.html",
        {"familiares": [familiar1, familiar2, familiar3]},
    )
