from dominio.cola import Cola

cola = Cola()

# lista vacia
# print(cola.preguntar_esta_vacia())

cola.encolar("batman")
cola.encolar("superman")
cola.encolar("mujer maravilla")
cola.encolar("acuaman")
cola.encolar("robin")
cola.encolar("linterna verde")

cola.ver_siguiente()

cola.desencolar()
cola.desencolar()
cola.ver_siguiente()
