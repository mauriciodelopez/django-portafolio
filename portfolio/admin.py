from django.contrib import admin
from .models import Project #Aqui agrego from models importar el project

# Register your models here.

admin.site.register(Project) #desde admin voy a ejecutar su modulo site, y voy a ejecutar la funcion register y desde ahi vas a anadir project que esta entre parentesis y ya importado arriba con from
