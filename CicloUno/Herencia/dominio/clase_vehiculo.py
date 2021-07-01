class Vehiculo(object):
    def __init__(self, modelo, color, aceleracion, velocidad):
        self.modelo = modelo
        self.color = color
        self.aceleracion = aceleracion
        self.velocidad = velocidad

    def acelerar(self, cambio):
        print("El vehículo está acelerando")
        cambio_velocidades = self.meter_cambios(cambio)

        for cambio in cambio_velocidades:
            print(cambio)
        self.velocidad = cambio_velocidades[-1]
        return self.velocidad

    def frenar(self):
        self.velocidad = self.velocidad - self.aceleracion
        if self.velocidad:
            print("El vehículo está quieto")
        return self.velocidad

    def meter_cambios(self, cambio):
        cambios_del_vehiculo = {
            "primera": list(range(0, 20)),
            "segunda": list(range(20, 50)),
            "tercera": list(range(50, 100)),
        }
        cambio_velocidades = cambios_del_vehiculo[cambio]
        return cambio_velocidades
