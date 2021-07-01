from dominio.clase_cola import Cola

cola = Cola()

# estado de la cola
print(cola.decir_tamano())
print(cola.preguntar_si_vacia())

# encolamiento
cola.encolar("batman")
cola.encolar("superman")
cola.encolar("mujer maravilla")
cola.encolar("linterna verde")

# estado de la cola
print(cola.decir_tamano())
cola.ver_cola()
cola.ver_siguiente()

# la cola avanza
cola.desencolar()
cola.ver_cola()
cola.desencolar()
cola.ver_cola()
cola.desencolar()
cola.ver_cola()
