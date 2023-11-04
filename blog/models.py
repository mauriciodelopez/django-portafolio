from django.db import models
import datetime

# Create your models here.
#esto hereda desde models.model
class Post(models.Model): 
    title = models.CharField(max_length=200)#el charField lo importo desde models, porque en models ya esta todo creado
    content = models.TextField()
    image = models.ImageField(upload_to='blog/images')#se crea otra carpeta para que no las mezcle con las de media
    date_posted = models.DateField(datetime.date.today)#si no colocan la fecha coloca la fecha actual
    
    
#para que aparezca en admin tengo que ir a admin y hacerlo