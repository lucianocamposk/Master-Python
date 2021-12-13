"""

FOR
 
 for variable in elemtno_iterable (lista, rango, etc)
        BLOQUE DE INSTRUCCIONES

"""
contador = 0
resultado=0
for contador in range(0,5):
    print("voy por el "+ str(contador))
    #resultado = resultado+contador
    resultado += contador
print(f"El resultado es: {resultado}")

#Ejemplo de for

print("\n########## EJEMPLO ##########")
 
numero_usuario= int(input("de que numero quieres la tabla?: "))

if numero_usuario<1:
    numero_usuario=1

print(f"\n### TABLA DE MULTIPLICAR DEL NRO {numero_usuario} ###")

for numero_tabla in range (1,11):

    if numero_usuario==45:
        print("no se puede mostrar nros prohibidos")
        break


    print(f"{numero_usuario} X {numero_tabla} = {numero_usuario*numero_tabla}")
else:
    print("Tabla finalizada.")