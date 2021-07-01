class Motor(object):
    def __init__(self, tipo_motor, tiempos):
        self.tipo = tipo_motor
        self.tiempos = tiempos

    def prender(self):
        motor_encendido = True
        print("brumm brumm")
        return motor_encendido

    def apagar(self):
        motor_encendido = False
        print("cuchu cuchu cof cof prrrrr")
        return motor_encendido
