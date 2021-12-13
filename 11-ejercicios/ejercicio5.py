"""
Ejercicio 5.
Crear una lista con el contenido de esta tabla:
ACCION   AVENTURA  DEPORTES
GTA      ASSASIN    FIFA 21
COD      CRASH      PES21
PUBG     PRINCE PERSIA      MOTO GP 21
"""
tabla=[

    {
        "categoria": "ACCION",
        "juegos":["GTA", "COD", "PUBG"]
    },
     {
        "categoria": "AVENTURA",
        "juegos":["ASSASSINS", "CRASH", "PRINCE PERSIA"]
    },
    {
        "categoria": "DEPORTES",
        "juegos":["FIFA 21", "PES 21", "MOTO GP 21"]
    },  
]

for categoria in tabla:
    print(f"-------- {categoria['categoria']}")
    for juego in categoria['juegos']:
        print(juego)