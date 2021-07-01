class Llanta(object):
    def __init__(self, tipo_llanta, llanta_sin_aire):
        self.tipo_llanta = tipo_llanta
        self.llanta_sin_aire = llanta_sin_aire

    def pinchada(self):
        self.llanta_sin_aire = True
        print("kusso!!! nos pinchamos")

    def inflar(self):
        self.llanta_sin_aire = False
        print("Llanta calibrada")
