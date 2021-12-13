"""
# Condicional IF

#operadores de comparacion

== igual
!= diferente
< menor que
> mayor que
<= menor o igual que
>= mayor o igual que

#operadores logicos

and Y
or O
! negacion
not NO


"""





#color= input("Adivina cual es mi color favorito: ")
color = "rojo"
if color == "rojo":
    print("Asi es mi color fav es el rojo")

else:
    print("color incorrecto")

#Ejemplo 3

print("\n########### EJEMPLO 3 ########")

nombre= "Luciano Campos"
ciudad = "Galvez"
Continente="Latinoamerica del sur"
edad= 55
mayoria_edad=18

if edad >= mayoria_edad:
    print(f"{nombre} es mayor de edad")

    if Continente != "Latinoamerica del sur":
        print("el usuario no es latino")
    else:
        print(f"es latino y de {ciudad}")

else:
    print(f"{nombre} No es mayor de edad")
    
print("\n########### EJEMPLO 4 ########")

#elif

#dia= int(input("Introducir numero del dia de la semana: "))
dia=2
if dia==1:
    print("Es lunes")
elif dia==2:
    print("Es martes")
elif dia==3:
    print("es miercoles")
elif dia==4:
    print(" es jueves")
elif dia == 5:
    print("es viernes")
else:
    print("es fin de semana")

print("\n########### EJEMPLO 5 ########")

edad_minima=18
edad_maxima=65
#edad_oficial=int(input("Escribe tu edad:"))
edad_oficial=20
if edad_oficial >= 18 and edad_oficial <= 65:
    print("Esta en edad de trabajar")
else:
    print("no esta en edad de trabajar")

print("\n########### EJEMPLO 6 ########")

pais= "España"

if not (pais=="mexico" or pais=="España"):
    print(f"{pais} no es un pais de habla hispana ")
else: print(f"{pais} si es un pais de habla hispana")

print("\n########### EJEMPLO 6 ########")

pais= "colombia"

if  pais != "colombia" and pais!="España":
    print(f"{pais} no es un pais de habla hispana ")
else: print(f"{pais} si es un pais de habla hispana")
