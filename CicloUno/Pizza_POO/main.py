from dominio.clase_pizza import Pizza
from dominio.menu import Menu
from Funciones.opc import opc

tipo = opc()

#Pizza vegetariana
if tipo == "1":
    ingrediente = Menu.mostrar_menu_vegetariana()
    pedido = Pizza("Vegetariana", ingrediente, Pizza.mostrar_tamano())
    pedido.servir_pizza()

else:
    ingrediente = Menu.mostrar_menu_no_vegetariana()
    pedido = Pizza("NO vegetariana", ingrediente, Pizza.mostrar_tamano())
    pedido.servir_pizza() 

