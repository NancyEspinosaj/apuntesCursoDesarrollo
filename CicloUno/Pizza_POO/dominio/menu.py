class Menu(object):
    def __init__(self):
        self.ingredientes_vegetariana = {1: "Pimiento", 2: "Tofu"}
        self.ingredientes_no_vegetariana = {1: "Peperoni", 2: "Jamón", 3: "Salmón"}
        self.mensaje_vegetariana = "Ingredientes de pizzas vegetarianas" + str(
            self.ingredientes_vegetariana
        )
        self.mensaje_no_vegetariana = "Ingredientes de pizzas no vegetarianas" + str(
            self.ingredientes_no_vegetariana
        )

    def mostrar_menu_vegetariana(self):
        print(self.mensaje_vegetariana)
        ingrediente = self.solicitar_ingrediente()
        return self.ingredientes_vegetariana[ingrediente]

    def mostrar_menu_no_vegetariana(self):
        print(self.mensaje_no_vegetariana)
        ingrediente = self.solicitar_ingrediente()
        return self.ingredientes_no_vegetariana[ingrediente]

    def solicitar_ingrediente(self):
        ingrediente = int(input("Introduce el ingrediente que desea: "))
        return ingrediente