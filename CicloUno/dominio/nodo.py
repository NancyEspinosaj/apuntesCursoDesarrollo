class Nodo(object):
    """obtener_link indica el nodo siguiente"""

    def __init__(self, dato):
        self.dato = dato
        self.link = None

    def obtener_dato(self):
        return self.dato

    def obtener_nodo_siguiente(self):
        return self.link

    def asignar_dato(self, nuevo_dato):
        self.dato = nuevo_dato

    def asignar_nodo_siguiente(self, nuevo_link):
        self.link = nuevo_link
