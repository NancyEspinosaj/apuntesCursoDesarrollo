from dominio.clase_vehiculo import Vehiculo
from dominio.clase_motor import Motor
from dominio.clase_llanta import Llanta


class Carro(Vehiculo, Motor, Llanta):
    def __init__(
        self,
        modelo,
        color,
        aceleracion,
        velocidad,
        tipo_motor,
        tiempos,
        exp,
        tipo_llanta,
        llanta_sin_aire,
    ):
        self.exp = exp
        Vehiculo.__init__(self, modelo, color, aceleracion, velocidad)
        Motor.__init__(self, tipo_motor, tiempos)
        Llanta.__init__(self, tipo_llanta, llanta_sin_aire)
        print(
            "Modelo: {}, Tiempos: {}, Motor: {}".format(
                self.modelo, self.tipo_llanta, self.exp
            )
        )

    def encender(self):
        print("encendiendo carro")
        self.encendido = Motor.prender(self)
        Llanta.inflar(self)
        self.arrancar("primera")

    def arrancar(self, cambio):
        if self.encendido:
            Vehiculo.acelerar(self, cambio)
