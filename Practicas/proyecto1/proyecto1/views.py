from pipes import Template
from django.http import HttpResponse
from django.template import Template, Context

def saludo(request):
    return HttpResponse("Saludos")

def probandoTemplate(self):
    miHtml = open(r'I:\taro\practicas django\DJANGO\Practicas\proyecto1\proyecto1\plantillas\template1.html')

    plantilla = Template(miHtmk.read())
    miHtml.close()

    miContexto = Context()
    documento = plantilla.render(miContexto)

    return HttpResponse(documento)