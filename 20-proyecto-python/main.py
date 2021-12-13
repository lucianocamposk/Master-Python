"""
Proyecto Python y Mysql
- Abrir asistente
- Login o registro
- Si elegimos registro, creara un usuario en la bdd
- Si elegimos login, identifica al usuario y nos preguntara
- Crear nota, mostrar notas, borrarlas y salir

"""

from usuarios import acciones

print("""
Acciones disponibles:
     - Registro
     - Login
""")

hazEl= acciones.Acciones()
accion = input("¿Que quieres hacer?: ")

if accion == 'registro':
    hazEl.registro()

elif accion == 'login':
    hazEl.login()