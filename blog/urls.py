
#desde django voy a importar su metodo llamado path

from django.urls import path
#importo el nombre de la vista que quiero enlazar con mi url la funcion render_posts
from .views import render_posts, post_detail

#aqui voy a definirlo crear una urlpatterns y esto va a ser igual
#voy a crear un arreglo que cuando visiten la ruta inicial de algo
#voy a renderisar posts y le vamos a colocar el name posts
#basicamente le digo que cuando visiten la pagina inicial renderise post

app_name = 'blog'

urlpatterns = [path("",render_posts, name="posts"), 
               path("<int:post_id>", post_detail, name="post_detail"),   
]

#esto no es para la aplicaion entera es simplemente para el blog,
#para la aplicacion entera tengo que ir a urls de mauro_portafolio
#y escribir la ruta un path
#luego de haber creado la ruta en el blog/, todo lo que vaya a crear aqui sera leido
#en urls.py mauro_portafolio a travez de la fuincion include
#todas van a iniciar con blog/
