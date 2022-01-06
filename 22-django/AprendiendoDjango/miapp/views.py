from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
# MVC = Modelo Vista Controlador -> Acciones (metodos)
# MVT = Modelo Template Vista    -> Acciones (metodos)

def hola_mundo(request):
    return render(request,'hola_mundo.html')
  
def index(request):

    html = """
        <h1>Inicio</h1>
        <p>Años hasta el 2050:</p>
    """
    year= 2021
    while year <= 2050:
        if year%2 ==0:
            html += f'<li>{str(year)}</li>'
        
        year +=1
    nombre = 'Luciano Campos Kriegl'
    return render(request,'index.html',{'title': 'Inicio',
    'mi_variable' : 'Soy un dato que esta en la vista',
    'nombre' : nombre})

def pagina(request, redirigir=0):
    if redirigir==1:
        return redirect('/inicio/')
    return render(request, 'pagina.html')

def contacto(request,nombre="",apellidos=""):
    html =""

    if nombre and apellidos:
        html += "<p>El nombre completo es:</p>"
        html += f"<h3>{nombre} {apellidos}<h3>"
        
    return HttpResponse(layout+ f"<h2>Contacto</h2>"+html)
      