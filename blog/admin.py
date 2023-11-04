from django.contrib import admin
from .models import Post

#desde models importo el modelo de publicacion

# Register your models here.

admin.site.register(Post)

#aqui le digo entre parentesis, quiero que utilices el modelo post
