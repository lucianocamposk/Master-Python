"""
Ejercicio3. programa que compruebe si una variable esta vacia
y si esta vacia, rellenarla con texto en minusculas y
mostrarla en mayuscula
"""

texto = " "

if len(texto.strip()) >= 0:

    texto = "hola soy un texto en minusculas o no"
    print(texto.upper())
else:
    print(f"La variable tiene el contenido: {texto}")
