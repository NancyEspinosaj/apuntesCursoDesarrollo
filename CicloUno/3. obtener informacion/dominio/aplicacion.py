from tkinter import *
from tkinter import ttk

# La clase 'Aplicacion' ha crecido. En el ejemplo se incluyen
# nuevos widgets en el método constructor __init__(): Uno de
# ellos es el botón 'Info'  que cuando sea presionado llamará 
# al método 'ver_informacion' para mostrar información en el otro 
# widget, una caja de texto: un evento ejecuta una acción: 

class Aplicacion():
    def __init__(self):
        
        
        self.ventana_principal = Tk()
        self.ventana_principal.geometry('300x200')
        
        # Impide que los bordes puedan desplazarse para
        # ampliar o reducir el tamaño de la ventana 'self.ventana_principal':
        
        self.ventana_principal.resizable(width=False,height=False)
        self.ventana_principal.title('Ver información')
        
        # Define el widget Text 'self.texto_informacion ' en el que se
        # pueden introducir varias líneas de texto:
        
        self.texto_informacion = Text(self.ventana_principal, width=40, height=10)
        
        # Sitúa la caja de texto 'self.texto_informacion' en la parte
        # superior de la ventana 'self.ventana_principal':
        
        self.texto_informacion.pack(side=TOP)
        
        # Define el widget Button 'self.boton_informacion' que llamará 
        # al metodo 'self.ver_informacion' cuando sea presionado
        
        self.boton_informacion = ttk.Button(self.ventana_principal, text='Info', 
                                command=self.ver_informacion)
        
        # Coloca el botón 'self.boton_informacion' debajo y a la izquierda
        # del widget anterior
                                
        self.boton_informacion.pack(side=LEFT)
        
        # Define el botón 'self.boton_salir'. En este caso
        # cuando sea presionado, el método destruirá o
        # terminará la aplicación-ventana 'self.raíz' con 
        # 'self.ventana_principal.destroy'
        
        self.boton_salir = ttk.Button(self.ventana_principal, text='Salir', 
                                 command=self.ventana_principal.destroy)
                                 
        # Coloca el botón 'self.boton_salir' a la derecha del 
        # objeto anterior.
                                 
        self.boton_salir.pack(side=RIGHT)
        
        # El foco de la aplicación se sitúa en el botón
        # 'self.boton_informacion' resaltando su borde. Si se presiona
        # la barra espaciadora el botón que tiene el foco
        # será pulsado. El foco puede cambiar de un widget
        # a otro con la tecla tabulador [tab]
        
        self.boton_informacion.focus_set()
        self.ventana_principal.mainloop()
    
    def ver_informacion(self):
        
        # Borra el contenido que tenga en un momento dado
        # la caja de texto
        
        #"1.0" y "end" se refieren al primer y último carácter del contenido del widget Text
        self.texto_informacion.delete("1.0", END)
        
        # Obtiene información de la ventana 'self.ventana_principal':
        
        clase_ventana = self.ventana_principal.winfo_class()
        resolucion_posicion = self.ventana_principal.winfo_geometry()
        ancho_ventana = str(self.ventana_principal.winfo_width())
        alto_vantana = str(self.ventana_principal.winfo_height())
        posicion_x = str(self.ventana_principal.winfo_rootx())
        posicion_y = str(self.ventana_principal.winfo_rooty())
        ventana_id = str(self.ventana_principal.winfo_id())
        nombre_objeto = self.ventana_principal.winfo_name()
        gestor_ventana = self.ventana_principal.winfo_manager()
        
        # Construye una cadena de texto con toda la
        # información obtenida:
        
        texto_info = "Clase de 'ventana_principal': " + clase_ventana + "\n"
        texto_info += "Resolución y posición: " + resolucion_posicion + "\n"
        texto_info += "Anchura ventana: " + ancho_ventana + "\n"
        texto_info += "Altura ventana: " + alto_vantana + "\n"
        texto_info += "Pos. Ventana X: " + posicion_x + "\n"
        texto_info += "Pos. Ventana Y: " + posicion_y + "\n"
        texto_info += "Id. de 'ventana_principal': " + ventana_id + "\n"
        texto_info += "Nombre objeto: " + nombre_objeto + "\n" 
        texto_info += "Gestor ventanas: " + gestor_ventana + "\n"
        
        # Inserta la información en la caja de texto:
        
        self.texto_informacion.insert("1.0", texto_info)

