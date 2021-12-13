import clases

persona = clases.Persona()
persona.setNombre('Victor')
persona.setApellidos('Robles')
persona.setAltura('190cm')
persona.setEdad('900 años')

print(f"La persona es: {persona.getApellidos()} {persona.getNombre()}")
print(persona.hablar())
print('-------------------------------')

informatico = clases.Informatico()
informatico.setNombre('Carlos')
informatico.setApellidos('Santana')

print(f"El informatico es: {informatico.getNombre()}{informatico.getApellidos()}")
print(informatico.getLenguajes())
print(informatico.caminar())
print(informatico.experiencia)
print('-------------------------------')

tecnico = clases.TecnicoRedes()
tecnico.setNombre('Manolo')
print(tecnico.auditarRedes,tecnico.getLenguajes(), tecnico.getNombre())