from django.http import HttpResponse
from django.shortcuts import render
from django.template import Template,Context,loader
from Familia.models import Familia

# Create your views here.
def templatefamilia(self):
    flia = Familia(nombre="Jorge",age=63,born="1960-11-21",rango="Padre")
    flia.save()
    documento = f"---> Nombre: {flia.nombre}    edad: {flia.age}   nacimiento: {flia.born}   rango: {flia.rango}"

    return HttpResponse(documento)



def familia_con_loader(self):
    flia = Familia(nombre="Jorge",age=63,born="1960-11-21",rango="Padre")
    flia.save()
    documento = f"---> Nombre: {flia.nombre}    edad: {flia.age}   nacimiento: {flia.born}   rango: {flia.rango}"

    temp = loader.get_template('template1.html')
    doc = temp.render()
    return HttpResponse(doc)

def all_family(self):

    template = loader.get_template('all_family.html')

    all_flia = Familia.objects.all()

    print('familiares', type(all_flia), '\n', all_flia)
    context_dict = {
        'familiares': all_flia
    }

    render = template.render(context_dict)
    return HttpResponse(render)
