from dominio.lista_ligada import ListaLigada


class Pila(ListaLigada):
    def __init__(self):
        super().__init__()

    def apilar_nodo(self, dato):
        self.agregar_dato(dato) #agregar_nodo
        print("--------------")
        self.mostrar_lista()
        print("--------------")

    def mostrar_tope(self):
        return self.primer_valor.obtener_dato() #primer_valor -> nodo_cabeza

    def desapilar_nodo(self):
        self.remover(self.mostrar_tope()) #remover_nodo
        print("xxxxxxxxxxxxxx")
        self.mostrar_lista()
        print("xxxxxxxxxxxxxx")
