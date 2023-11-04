from django.shortcuts import render, get_object_or_404
from .models import Post

def render_posts(request): #permite de renderisar todas las publicaciones
    posts = Post.objects.all()
    return render(request, 'posts.html', {'posts': posts})

#ahora voy a tener una lista que va a renderisar un detalle de publicacion
#y me va a retornar post_detail.html que voy a crear en templates 
def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id) #entre parentesis les paso el modelo que quiero buscar que es Post y le paso una priary key =y le indico lo que quiero buscar en este caso el post_id
    return render(request, 'post_detail.html', {"post":post})#te paso una variable que se llama post y tiene como valor post_deatil


#si va a la database y no encuentra id tiene que decir error 
#desde post quiero traer todos los objetos 
#la funcion request va retornar el posts.html
#como lo hago voy a urls.py
#utlizo un diccionario que me devuelve como valor lo que esta en la database
#si yo quiero ver esto voy a post.html 
