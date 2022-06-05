from pipes import Template
import datetime
from django.http import HttpResponse
from django.template import Template, Context
from django.template import loader


#en mi vista... hago las funciones que quiero que aparezcan en mi pagina... una vez hecho
#voy a URLS y lo importo...
def saludo(request):
    return HttpResponse("que onda brotherrrr")

def segunda_vista(request):
    return HttpResponse("<br><h3>anashei<h3><br>")

def dia_hoy(request):
    dia = datetime.datetime.now()

    documentoDeTexto = f"hoy es día: <br> {dia}"

    return HttpResponse(documentoDeTexto)

def mi_nombre(self, nombre):
    documentoDeTexto = f"Hola, mi nombre es: <h4><br> {nombre}"
    return HttpResponse(documentoDeTexto)

def primer_template(self):

    nom = "Lauti"
    ap= "Rossi"

    tiempo = datetime.datetime.now

    lista_notas = [1,2,5,6,2,45]

    diccionario = {"nombre": nom, "apellido": ap, "tiempo": tiempo, "notas":lista_notas} #--- para emviar al contexto

    #miHtml = open(r"I:\taro\practicas-django\Practicas\proyecto1\proyecto1\plantillas\template1.html")

    #plantilla = Template(miHtml.read())
    #miHtml.close()

    #miContexto = Context(diccionario) #-- aca mandamos el diccionario
    #documento = plantilla.render(miContexto)

    #Mejora con cargadores.
    plantilla = loader.get_template("template1.html")
    documento = plantilla.render(diccionario)
    return HttpResponse(documento)