
from django.template import Context, Template, loader
from django.http import HttpResponse

import random

def saludo_con_template(request):
    #mi_archivo = open("C:\Users\marti\Documents\GitHub\MVT-MARTINFURON\MVTMartinFuron\MVTMartinFuron\templates\template1.html")
    template = loader.get_template("template1.html")
    #mi_archivo.close()
    dic = {"var1": ""}
    plantilla1 = template.render(dic)
    return HttpResponse(plantilla1)

def saludo(request):
    return HttpResponse("hola Coder")
