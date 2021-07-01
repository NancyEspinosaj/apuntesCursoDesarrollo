from tkinter import *
from tkinter import ttk

class VentanaPrincipal():
    """ 
    Crea una clase Python para definir el interfaz de usuario de
    la aplicacion
    """
    def __init__(self):
        """construye y muestra la ventana con todos sus widgets"""
        ventana_principal = Tk()
        ventana_principal.geometry('300x200')
        ventana_principal.configure(bg = 'beige')
        ventana_principal.title('Aplicación')
        ttk.Button(ventana_principal, text='Salir', 
                   command=ventana_principal.destroy).pack(side=BOTTOM)
        ventana_principal.mainloop()