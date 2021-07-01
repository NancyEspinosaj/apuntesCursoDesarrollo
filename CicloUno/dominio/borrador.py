from dominio.clase_vehiculo import Vehiculo
from dominio.clase_llanta import Llanta
from dominio.clase_motor import Motor


class Carro(Vehiculo, Llanta, Motor):
    """definimos la clase carro con herencia compuesta"""

    def __init__(
        self,
        modelo,
        color,
        aceleracion,
        velocidad,
        tipo_llanta,
        llanta_sin_aire,
        tipo_motor,
        tiempos,
        volante,
    ):
        self.volante = volante

        Vehiculo.__init__(self, modelo, color, aceleracion, velocidad)

        Llanta.__init__(self, tipo_llanta, llanta_sin_aire)

        Motor.__init__(
            self,
            tipo_motor,
            tiempos,
        )

    def encender(self):
        print("encendiendo carro")
        self.encendido = Motor.prender()
        Llanta.inflar()
        self.arrancar("primera")

    def arrancar(self, cambio):
        if self.encendido:
            Vehiculo.acelerar(cambio)
