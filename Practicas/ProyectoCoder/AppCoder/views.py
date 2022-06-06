from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from AppCoder.models import curso

# Create your views here.
def Curso(self):

    Curso = curso(nombre = "Desarrollo Web", camada = "19981")
    Curso.save()
    documentoDeTexto = f"--> Curso: {Curso.nombre}  Camada : {Curso.camada}" 

    return HttpResponse(documentoDeTexto)


def cursos(request):
    return render(request,"AppCoder/cursos.html")

def profesores(request):
    return render(request,"AppCoder/profesores.html")

def estudiantes(request):
    return render(request,"AppCoder/estudiantes.html")

def entregables(request):
    return render(request,"AppCoder/entregables.html")

#def inicio(self):
 #   plantilla = loader.get_template("AppCoder/inicio.html")
  #  documento = plantilla.render()
   # return HttpResponse(documento)

def inicio(request):
    return render(request,"AppCoder/inicio.html")
    
    