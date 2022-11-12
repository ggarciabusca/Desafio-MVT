from django.http import HttpResponse
from django.template import Template, Context, loader
from app1.models import Persona
#from django.shortcuts import render
# Create your views here.

def listado_familiares(request): #función que devuelve el listado de familiares
    
    #leo todos los datos de la tabla app1-persona
    #esto es una lista de instancias de la clase "Persona" en la base de datos
    personas = Persona.objects.all() 

    archivo = open(r"E:\Gonzalo\Python\Desafio\desafio_mvt\app1\templates\app1\listado_personas.html")
    plantilla = Template(archivo.read())
    archivo.close

    diccionario_familiares = {"familiares":personas}

    contexto = Context(diccionario_familiares)

    documento = plantilla.render(contexto)
    return HttpResponse(documento)

    #return render(request, "app1/listado_personas.html",)











# Armo la lista de familiares a devolver al formulario
#    cadena_respuesta = "<ul>"
#    for persona in personas:
#         cadena_respuesta += f"<li>{persona.nombre}, DNI: {persona.dni}, Fecha nacido:{persona.nacido} </li>"
#    cadena_respuesta += "</ul>"

#    return HttpResponse(cadena_respuesta)

#<a href="{% url 'coder-inicio'%}"> Ir a inicio </a>