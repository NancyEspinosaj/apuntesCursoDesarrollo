from dominio.lista_ligada import ListaLigada


class Cola(ListaLigada):
    def __init__(self):
        super().__init__()

    def encolar(self, dato):
        self.agregar_dato(dato)
        print("--------------")
        self.mostrar_lista()
        print("--------------")

    def ver_siguiente(self):
        dato_a_validar = self.primer_valor
        while dato_a_validar is not None:
            siguiente = dato_a_validar.obtener_dato()
            dato_a_validar = dato_a_validar.obtener_nodo_siguiente()
        print("ooooooooooooooo")
        print(siguiente)
        print("ooooooooooooooo")
        return siguiente

    def desencolar(self):
        self.remover(self.ver_siguiente())
        print("xxxxxxxxxxxxxxx")
        self.mostrar_lista()
        print("xxxxxxxxxxxxxxx")
