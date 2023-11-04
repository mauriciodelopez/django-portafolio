from django.shortcuts import render
#el render es para decirle que pagina va a ser mostrada
#seria renderisar a travez de request
from .models import Project #traigo el modelo de datos que he definido dentro de portfolio

# Create your views here.

def home(request):  
    projects = Project.objects.all() #meto todo dentro de una variable llamada projects
     
    return render (request, 'home.html', {'projects' : projects })

#esto recibe un request, abajo va a recibir la logica de que retornar con return
#en django todo el elemento que contenga html django sabe que es un template  el render de aqui ya conoce la carpeta templates 
    
    