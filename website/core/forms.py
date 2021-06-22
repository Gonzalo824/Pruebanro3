from django import forms
from django.forms import ModelForm 
from .models import Biblioteca

class BibliotecaForm(ModelForm):
    
    class Meta:
        model = Biblioteca
        fields = ['isbn', 'nombre', 'autor', 'descripcion', 'categoria',]