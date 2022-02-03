from ast import For
from turtle import title
from django.shortcuts import render, HttpResponse, redirect
from miapp.models import Article, Category
from django.db.models import Q
from miapp.forms import FormArticle
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

    
    if request.method == 'POST':
            
        title = request.POST['title']

        if len(title) <= 5:
            return HttpResponse('Titulo demasiado corto')

        content =  request.POST['content']
        public = request.POST['public']

        articulo = Article(
            title = title,
            content = content,
            public = public
        )

        articulo.save()
        return HttpResponse(f'Articulo creado: <strong> {articulo.title}, {articulo.content} </strong> ')

    else: 
        
        return HttpResponse("<h2>No se ha podido crear el articulo</h2>")


def create_article(request):
   
    return render(request, 'create_article.html')


def create_full_article(request):

    if request.method == 'POST':
    
        
        formulario =  FormArticle(request.POST)

        if formulario.is_valid():
            data_form = formulario.cleaned_data
            
            title = data_form.get('title')
            content = data_form['content']
            public = data_form['public']

            articulo = Article(
            title = title,
            content = content,
            public = public
             )

            articulo.save()
            return redirect('articulos')
            #return HttpResponse (articulo.title + '-' + articulo.content + '-' + str(articulo.public))
    else:
       formulario = FormArticle()
        
    return render(request,'create_full_article.html',{
        'form' : formulario
        })


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
    
    articulos = Article.objects.all().order_by('-id')
    # lookups para ir filtrando
    #articulos = Article.objects.filter(id__lte=14, title__contains='articulo')
    
    """
    articulos = Article.objects.filter(
        Q(title__contains="2") | Q(title__contains="3")
        )

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