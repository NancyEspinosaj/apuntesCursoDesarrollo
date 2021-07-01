class Cola:
    def __init__(self):
        self.items = []

    def preguntar_si_vacia(self):
        return self.items == []

    def encolar(self, item):
        self.items.insert(0, item)

    def desencolar(self):
        return self.items.pop()

    def decir_tamano(self):
        return len(self.items)

    def ver_cola(self):
        print(self.items)

    def ver_siguiente(self):
        print(self.items[-1])
