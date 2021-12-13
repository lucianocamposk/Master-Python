# Capturar excepciones y manejar errores en codigo
# Susceptible a fallos / errores

"""
try:
    nombre= input("¿Cual es tu nombre: ")

    if len(nombre) > 1:
        nombre_usuario='El nombre es' + nombre

    print(nombre_usuario)

except:
    print('Ha ocurrido un error, mete bien el nombre')
else:
    print('Todo ha funcionado correctamente')
finally:
    print('Fin de la iteracion')

    """

# Multiples excepciones
"""
try:
    numero = int(input('Numero para elevarlo al cuadrado: '))
    print('el cuadrado es: ' +str(numero*numero))
except TypeError:
    print('Debes convertir tus cadenas a enteros en el codigo')
#except ValueError:
#    print('Introduce un numero correcto')
except Exception as e:
    print(type(e))
    # o sino mejor
    print('Ha ocurrido un error: ', type(e).__name__)
"""


#Excepciones personalizadas o lanzar una excepcion

try:
    nombre = input('Intoduce el nombre: ')
    edad = int(input('Introdue la edad: '))

    if edad <5 or edad > 110:
        raise ValueError('La edad introducida no es real')
    elif len(nombre)<=1:
        raise ValueError('El nombre no esta completo')
    else:
        print(f"Bienvenido al master en python {nombre} !!")
except ValueError:
    print('Introduce los datos correctamente')
except Exception as e:
    print('Existe un error: ', e)