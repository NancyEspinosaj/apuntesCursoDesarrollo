from dominio.nodo import Nodo


class ListaLigada(object):
    def __init__(self):
        self.primer_valor = None
        # nodo

    def preguntar_esta_vacia(self):
        # return self.primer_valor == None
        return self.primer_valor is None

    # ListaLigada.agregar_dato(31)
    def agregar_dato(self, dato):
        nodo = Nodo(dato)
        nodo.asignar_nodo_siguiente(self.primer_valor)
        self.primer_valor = nodo

    def decir_tamano(self):
        dato_a_validar = self.primer_valor
        contador = 0
        while dato_a_validar is not None:
            contador = contador + 1
            dato_a_validar = dato_a_validar.obtener_nodo_siguiente()

        return contador
