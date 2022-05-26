from pipes import Template
import datetime
from django.http import HttpResponse
from django.template import Template, Context

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

def probandoTemplate(self):
    miHtml = open(r'I:\taro\practicas django\DJANGO\Practicas\proyecto1\proyecto1\plantillas\template1.html')

    plantilla = Template(miHtmk.read())
    miHtml.close()

    miContexto = Context()
    documento = plantilla.render(miContexto)

    return HttpResponse(documento)