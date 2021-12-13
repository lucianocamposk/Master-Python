import os, shutil

# Crear carpeta
if not os.path.isdir("./mi_carpeta"):
    os.mkdir("./mi_carpeta")
else:
    print('ya existe el directorio')

# Copiar
"""
ruta_original= "./mi_carpeta"
ruta_nueva = "./mi_carpeta_COPIADA"

shutil.copytree(ruta_original,ruta_nueva)
"""
# Eliminar
"""
os.rmdir('./mi_carpeta_COPIADA')
"""

