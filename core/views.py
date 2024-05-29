from django.shortcuts import render
from django.views.generic import TemplateView


class Inicio(TemplateView):
    template_name="core/inicio.html"
    
    
class Informacion(TemplateView):
    template_name="core/acerca_de.html"