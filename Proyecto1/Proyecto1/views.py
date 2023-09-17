from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render

class Persona(object):
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

def saludo(request): #primera vista

    p1 = Persona("Juan Pedro", "Díaz")
    #nombre = "Juan"
    #apellido = "Díaz"
    ahora = datetime.datetime.now()
     #cargamos el documento directamente(Es mejor usar cargadores)
    #doc_externo = open("C:/Users/jadaj/Desktop/Django web/Proyecto1/Proyecto1/Plantillas/Miplantilla1.html")
    #doc_externo = get_template('Miplantilla1.html')
    #plt = Template(doc_externo.read())
    #creamos el objeto tipo Template y le hacemos leer el documento y lo cargamos
    #doc_externo.close()


    #una vez leido y cargado lo cerramos para no consumir recursos
    #ctx = Context({"nombre_persona":nombre, "apellido_persona":apellido, "momento_actual":ahora})
    temasDelCurso = ["Plantillas","Modelos","Formularios","Vistas","desplegue"]
    #ctx = Context({"nombre_persona":p1.nombre, "apellido_persona":p1.apellido, "momento_actual":ahora, "temas":["Plantillas","Modelos","Formularios","Vistas","desplegue"]})
    #ctx = Context({"nombre_persona":p1.nombre, "apellido_persona":p1.apellido, "momento_actual":ahora, "temas":temasDelCurso})
    #documento = doc_externo.render({"nombre_persona":p1.nombre, "apellido_persona":p1.apellido, "momento_actual":ahora, "temas":temasDelCurso})

    return render(request, "Miplantilla1.html",{"nombre_persona":p1.nombre, "apellido_persona":p1.apellido, "momento_actual":ahora, "temas":["Plantillas","Modelos","Formularios","Vistas","desplegue"]})

def despedida(request):
    return HttpResponse("Hasta luego alumnos")

def damefecha(reques):
    fecha_actual = datetime.datetime.now()
    documento = "<html><body><h1>Fecha y horas actuales  %s </h1></body></html>" % fecha_actual
    return HttpResponse(documento)

def calculaedad(request, edad, anio):
    
    periodo = anio - 2023
    edadfutura= edad + periodo
    documento = "<html><body><h1>En el año  %s tendras %s años </h1></body></html>" %(anio, edadfutura)
    return HttpResponse(documento)

def cursoc(request):
    fecha_actual = datetime.datetime.now()
    return render (request, "cursoc.html", {"dameFecha" : fecha_actual})

def cursocss(request):
    fecha_actual = datetime.datetime.now()
    return render (request, "cursocss.html", {"dameFecha" : fecha_actual})