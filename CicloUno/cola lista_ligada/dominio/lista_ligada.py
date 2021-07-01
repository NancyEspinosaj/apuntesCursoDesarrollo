from dominio.nodo import Nodo


class ListaLigada(object):
    def __init__(self):
        self.primer_valor = None

    def preguntar_esta_vacia(self):
        # return self.primer_valor == None
        return self.primer_valor is None

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

    def buscar(self, dato):
        dato_a_buscar = self.primer_valor
        dato_encontrado = False
        while dato_a_buscar is not None and not dato_encontrado:
            if dato_a_buscar.obtener_dato() == dato:
                dato_encontrado = True
            else:
                dato_a_buscar = dato_a_buscar.obtener_nodo_siguiente()

        return dato_encontrado

    def remover(self, dato_a_remover):
        dato_a_validar = self.primer_valor
        dato_previo = None
        dato_encontrado = False
        while not dato_encontrado:
            if dato_a_validar.obtener_dato() == dato_a_remover:
                dato_encontrado = True
            else:
                dato_previo = dato_a_validar
                dato_a_validar = dato_a_validar.obtener_nodo_siguiente()

        if dato_previo is None:
            self.primer_valor = dato_a_validar.obtener_nodo_siguiente()
        else:
            dato_previo.asignar_nodo_siguiente(dato_a_validar.obtener_nodo_siguiente())

    def mostrar_lista(self):
        dato_a_mostrar = self.primer_valor
        tamano = self.decir_tamano()
        for dato in range(tamano):
            print(dato_a_mostrar.obtener_dato())
            dato_a_mostrar = dato_a_mostrar.obtener_nodo_siguiente()
