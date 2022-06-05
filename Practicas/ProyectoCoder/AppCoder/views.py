from django.http import HttpResponse
from django.shortcuts import render

from AppCoder.models import curso

# Create your views here.
def Curso(self):

    Curso = curso(nombre = "Desarrollo Web", camada = "19981")
    Curso.save()
    documentoDeTexto = f"--> Curso: {Curso.nombre}  Camada : {Curso.camada}" 

    return HttpResponse(documentoDeTexto)