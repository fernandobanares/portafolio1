from django.shortcuts import render
from .models import Proyecto

def home(request):
    proyectos = Proyecto.objects.all()
    return render(request, 'home.html', {'proyectos': proyectos})

def sobre_mi(request):
    return render(request, 'sobre_mi.html')

def lista_proyectos(request):
    proyectos = Proyecto.objects.all()
    return render(request, 'proyectos.html', {'proyectos': proyectos})

def experiencia(request):
    return render(request, 'experiencia.html')