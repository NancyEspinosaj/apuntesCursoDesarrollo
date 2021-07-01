from dominio.clase_pizza import Pizza
from dominio.clase_menu import Menu
from aplicaciones.pedir_tamano import pedir_tamano
from aplicaciones.saludar import saludar

tipo = saludar()
porciones = pedir_tamano()
menu = Menu()


if tipo == "1":
    ingrediente = menu.mostrar_menu_vegetariana()
    pizza_preparada = Pizza("vegetariana", ingrediente, porciones)
    pizza_preparada.servir_pizza()


else:
    ingrediente = menu.mostrar_menu_no_vegetariana()
    pizza_preparada = Pizza("no vegetariana", ingrediente, porciones)
    pizza_preparada.servir_pizza()
