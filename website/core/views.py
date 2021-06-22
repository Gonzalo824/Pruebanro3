from django.shortcuts import render, redirect
from django.template import loader
from .models import Biblioteca
from .forms import BibliotecaForm



# Create your views here.
def home(request):
    bibliotecas = Biblioteca.objects.all()
    datos = {
        'Bibliotecas': bibliotecas
    }
    return render(request, 'core/home.html', datos)

def form_biblioteca(request):
    datos = {
        'form': BibliotecaForm()
    }
    if request.method == 'POST':
        formulario = BibliotecaForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Datos guardados correctamente"

    return render(request, 'core/form_biblioteca.html', datos)

def form_mod_biblioteca(request, id):
    biblioteca = Biblioteca.objects.get(isbn=id)
    datos = {
        'form': BibliotecaForm(instance=biblioteca)
    }
    if request.method == 'POST':
        formulario = BibliotecaForm(data=request.POST, instance=biblioteca)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Modificados correctamente"
    return render(request, 'core/form_mod_biblioteca.html', datos)

def form_del_biblioteca(request, id):
    biblioteca = Biblioteca.objects.get(isbn=id)
    biblioteca.delete()
    return redirect(to="home")

