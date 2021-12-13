"""
Diccionario:
Es un tipo de dato que almacena un conjunto de datos.
Es un formato clave > valor.
Es parecido a un arrai asociativo o un objeto json
"""

persona = {

    "nombre": "Victor",
    "apellidos": "Robles",
    "web": "victorroblesweb.es"
}

print(persona["apellidos"])

# Lista con diccionarios

contactos= [

    {
        'nombre': 'Antonio',
        'email': 'antonio@lantoniouis.com'

    },
    {
        'nombre': 'luis',
        'email': 'luis@luis.com'

    },
    {
        'nombre': 'salvador',
        'email': 'salvador@salvador.com'

    }


]
contactos[0]['nombre']= "Antoñito"
print(contactos[0]['nombre'])

print("\nListado de contactos: ")

for contacto in contactos:
    print(f"Nombre del contacto: {contacto['nombre']}")
    print(f"Email del contacto: {contacto['email']}")
    print("-----------------------------------")
