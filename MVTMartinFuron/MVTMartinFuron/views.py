
from django.template import Context, Template, loader
from django.http import HttpResponse

import random

def saludo_con_template(request):
    template = loader.get_template("template1.hml")

    context = Context()

    res = template.render(context)
    return HttpResponse(res)

def saludo(request):
    return HttpResponse("hola Coder")
