from dominio.clase_encapsulada import Encapsulada
from dominio.clase_sin_encapsular import NoEncapsulada

"""
 consiste en hacer que los atributos o métodos internos 
 a una clase no se puedan acceder ni modificar desde fuera,
 sino que tan solo el propio objeto pueda acceder a ellos.
"""


mi_clase = NoEncapsulada("Que tal")
print(mi_clase.atributo_clase)
print(mi_clase.atributo_instancia)
print("estoy sin encapsular")

print("Yo estoy encapsulada")
mi_clase = Encapsulada()
# mi_clase.__atributo_clase  # Error! El atributo no es accesible
# mi_clase.__mi_metodo()  # Error! El método no es accesible
mi_clase.metodo_normal()  # Ok!
