from dominio.ventana_principal import VentanaPrincipal
"""
Define la función main() que es en realidad la que indica 
el comienzo del programa. Dentro de ella se crea el objeto 
aplicación 'mi_app' basado en la clase 'VentanaPrincipal':
"""
def ejecutar():
    ventana = VentanaPrincipal()

# no sueles querer que se ejecute código si no llamas a 
# una función tu mismo y esa es la razón de usar

if __name__ == '__main__':
    ejecutar()
