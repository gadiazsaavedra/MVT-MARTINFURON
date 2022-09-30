
from django.shortcuts import render
from django.template import  loader
from django.http import HttpResponse

import random

def saludo_con_template(request):
    template = loader.get_template("template1.html")
    dic = {"var1": ""}
    res = template.render(dic)
    return HttpResponse(res)

def saludo(request):
    return HttpResponse("hola Coder")
# Create your views here.
