
from django.shortcuts import render
from django.template import  loader
from django.http import HttpResponse

import random

from App_MartinFuron.models import familia

# def saludo_con_template(request):
#     template = loader.get_template("template1.html")
#     dic = {"var1": ""}
#     res = template.render(dic)
#     return HttpResponse(res)

def saludo(request):
    return HttpResponse("hola Coder")

def mostrar_familia(request):
    template = loader.get_template("template1.html")
    var1 = familia(nombre="Marcelo", apellido="Furon", telefono="1141242154",email="marc@elos.com", mayor_de_edad= True, cumpleaños= "1960/01/02")
    var2 = familia(nombre="Pedro", apellido="Furon", telefono="23231444",email="pepe@elos.com", mayor_de_edad= False, cumpleaños= "2010/04/05")
    var3 = familia(nombre="Alejandra", apellido="Garcia", telefono="114456567",email="ale@jandra.com", mayor_de_edad= True, cumpleaños= "1960/09/31")
    dic= {
        "fam1": (f"Nombre completo: {var1.nombre} {var1.apellido}, teléfono : {var1.telefono}, email: {var1.email}, Mayor de edad : {var1.mayor_de_edad}, cumpleaños: {var1.cumpleaños}"),
        "fam2": (f"Nombre completo: {var2.nombre} {var2.apellido}, teléfono : {var2.telefono}, email: {var2.email}, Mayor de edad : {var2.mayor_de_edad}, cumpleaños: {var2.cumpleaños}"),
        "fam3": (f"Nombre completo: {var3.nombre} {var3.apellido}, teléfono : {var3.telefono}, email: {var3.email}, Mayor de edad : {var3.mayor_de_edad}, cumpleaños: {var3.cumpleaños}")
        }
    res = template.render(dic)
    return HttpResponse(res)


# Create your views here.
