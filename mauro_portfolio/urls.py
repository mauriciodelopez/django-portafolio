"""
URL configuration for mauro_portfolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include #este include lo que hace es poder leer nuestras carpetas
#y poder decir que es lo va a ser incluido /blog,
from django.conf.urls.static import static
from django.conf import settings
from portfolio import views
from blog import urls


#quiero renderisar la vista que viene desde portfolio 
#desde la app portfolio import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
#a las rutas se les puede colocar un nombre
#cuando valla a navegar aqui solo tengo que colocar home
    path('blog/',include('blog.urls'))
#cada vez que yo visite el /blog el va a entrar en blog urls,
#y va decir cuando visite la ruta /blog voy a renderizar
#con la funcion request de views  
#seria : urls.py(proyecto) va carpeta blog va urls.py(lee renderizar) 
# que viene de views.py, que dice lo que se hace en posts.html
#yo puedo crear mas rutas en el urls.py de blog y seran incluidas dentro de 
#la ruta /blog
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
