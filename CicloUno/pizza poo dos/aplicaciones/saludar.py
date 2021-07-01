def saludar():
    tipo_pizza = {1: "Vegetariana", 2: "No Vegetariana"}
    print("Bienvenido a la pizzeria Bella Napoli.\nTipos de pizza " + str(tipo_pizza))

    tipo = input("Introduce el número correspondiente al tipo de pizza que quieres:")
    return tipo
