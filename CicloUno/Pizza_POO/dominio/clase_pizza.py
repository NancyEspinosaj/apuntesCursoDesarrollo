class Pizza(object):
    """Clase que representa a una Pizza"""

    def __init__(self, nombre, ingredientes, tamano):
        """Constructor clase pizza"""
        self.ingredientes = ingredientes
        self.nombre = nombre
        self.tamano = tamano

    def preparar_pizza(self):
        pizza_preparada = (
            "Pizza " + self.nombre + " con " + self.ingredientes + " mozarela y tomate"
        )
        return pizza_preparada

    def mostrar_tamano(self):
        tipos_porciones = {1: 8, 2: 4}
        dimension = int(input("que tamaño desea?\n 1.Familiar\t 2. Personal"))
        return tipos_porciones[dimension]

    def servir_pizza(self):
        preparacion = self.preparar_pizza()
        pizza_cortada = self.mostrar_tamano()
        print(preparacion)
        print("la pizza es cortada en " + str(pizza_cortada) + " porciones")

    