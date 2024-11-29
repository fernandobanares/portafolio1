from django.shortcuts import render, redirect
from .models import Proyecto, Mensaje
from django.contrib import messages
from .forms import ContactoForm

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

def contacto(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            email = form.cleaned_data['email']
            asunto = form.cleaned_data['asunto']
            mensaje = form.cleaned_data['mensaje']

            # Aquí puedes guardar el mensaje en la base de datos o enviarlo por correo
            # Por ejemplo:
            Mensaje.objects.create(nombre=nombre, email=email, asunto=asunto, mensaje=mensaje)

            # Agregar un mensaje de éxito
            messages.success(request, '¡Tu mensaje ha sido enviado exitosamente!')
        else:
            # En caso de errores en el formulario
            messages.error(request, 'Por favor, corrige los errores e intenta nuevamente.')
    else:
        form = ContactoForm()
    return render(request, 'contacto.html', {'form': form})

