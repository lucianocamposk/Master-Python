from turtle import title
from django.shortcuts import render, HttpResponse, redirect
from miapp.models import Article, Category
from django.db.models import Q
# Create your views here.
# MVC = Modelo Vista Controlador -> Acciones (metodos)
# MVT = Modelo Template Vista    -> Acciones (metodos)

def hola_mundo(request):
    return render(request,'hola_mundo.html')
  
def index(request):
    """
    html = ""
        <h1>Inicio</h1>
        <p>Años hasta el 2050:</p>
    ""
    year= 2021
    while year <= 2050:
        if year%2 ==0:
            html += f'<li>{str(year)}</li>'
        
        year +=1
    """
    year = 2021
    hasta = range(year, 2052)
    nombre = 'Luciano Campos Kriegl'
    lenguajes = ['JavaScript','Python', 'PHP', 'C++']

    return render(request,'index.html',
    {'title': 'Inicio',
    'mi_variable' : 'Soy un dato que esta en la vista',
    'nombre' : nombre,
    'lenguajes' : lenguajes,
    'years' : hasta})

def pagina(request, redirigir=0):
    if redirigir==1:
        return redirect('/inicio/')
    return render(request, 'pagina.html',{
        'texto' : 'Este es mi texto',
        'lista' : ['uno', 'dos', 'tres']

    })

def contacto(request,nombre="",apellidos=""):
    html =""

    if nombre and apellidos:
        html += "<p>El nombre completo es:</p>"
        html += f"<h3>{nombre} {apellidos}<h3>"
        
      

def crear_articulo(request, title, content, public):

    articulo = Article(
        title = title,
        content = content,
        public = public
    )

    articulo.save()
    return HttpResponse(f'Articulo creado: <strong> {articulo.title}, {articulo.content} </strong> ')

def save_article(request):
    
    articulo = Article(
        title = title,
        content = content,
        public = public
    )

    articulo.save()
    return HttpResponse(f'Articulo creado: <strong> {articulo.title}, {articulo.content} </strong> ')

def create_article(request):
   
    return render(request, 'create_article.html')


def articulo(request):

    try:
        articulo = Article.objects.get(title="Superman", public=False)
        response = f"Articulo: <br/> {articulo.id}. {articulo.title}"
    except:
        response = "<h1> Articulo no encontrado </h1>"
    
    return HttpResponse(response)

def editar_articulo(request, id):

    articulo = Article.objects.get(pk=id)

    articulo.title = 'Batman'
    articulo.content = 'Pelicula del 2017'
    articulo.public = True

    articulo.save()

    return HttpResponse(f'Articulo {articulo.id} editado: <strong> {articulo.title}, {articulo.content} </strong> ')


def articulos(request):
    
    articulos = Article.objects.all()
    # lookups para ir filtrando
    #articulos = Article.objects.filter(id__lte=14, title__contains='articulo')
   
    articulos = Article.objects.filter(
        Q(title__contains="2") | Q(title__contains="3")
        )

    """
    articulos = Article.objects.filter(
                                             title='Articulo',
                                        ).exclude(
                                            public=False
                                        )
    """

    #articulos = Article.objects.raw("SELECT * FROM miapp_article WHERE title='Articulo' AND public=1")

    return render(request, 'articulos.html',{
        'articulos' : articulos
    })

def borrar_articulo(request,id):
    
    articulo = Article.objects.get(pk=id)
    articulo.delete()
    
    return redirect('articulos')