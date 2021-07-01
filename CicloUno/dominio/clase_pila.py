class Pila:
    """Clase Pila"""

    def __init__(self):
        self.datos = []

    def preguntar_si_vacia(self):
        return self.datos == []

    def apilar(self, item):
        self.datos.append(item)

    def desapilar(self):
        return self.datos.pop()

    def mostrar_tope(self):
        return self.datos[len(self.datos) - 1]

    def mostrar_tamano(self):
        return len(self.datos)

    def mostrar_pila(self):
        print(self.datos)
