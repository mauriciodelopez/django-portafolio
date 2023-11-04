from django.db import models
from django.db.models.fields import CharField, URLField #charfield se uiliza para caracteres
from django.db.models.fields.files import ImageField
#aqui tengo mi modelo de datos 

class Project(models.Model): #toma del models en la linea 1 y hereda Model, que nos permitira definir que queremos gurdar dentro del proyecto
    #propiedades, para cada proyecto que voy a crear este debe tener 
    title = CharField(max_length=100)
    description = CharField(max_length=250)
    image= ImageField(upload_to='portfolio/images')#vas a registrar la imagen cuando se cargue en una carpeta llmada porfolio y la vas a meter en imagenes
    url= URLField(blank=True)# es para evitar que tengan que colocar la url
