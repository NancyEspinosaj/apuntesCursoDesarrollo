class Nodo(object):
    """
    Clase nodo para lista ligada Simple
    donde el nodo está compuesto por un dato
    y un liga, en esta caso la liga se llama
    link.
    """

    def __init__(self, dato, link=None):
        self.dato = dato
        self.link = link

    # def __init__(self, dato):
    #     self.dato = dato
    #     self.link = None

    # regresar valores
    def obtener_dato(self):
        return self.dato

    def obtener_nodo_siguiente(self):
        return self.link

    # guardar
    def asignar_dato(self, nuevo_dato):
        self.dato = nuevo_dato

    def asignar_nodo_siguiente(self, nuevo_link):
        self.link = nuevo_link
