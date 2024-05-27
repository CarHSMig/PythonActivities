class Fila:
    def __init__(self):
        self.items = []

    def adicionar(self, item):
        self.items.append(item)

    def retirar(self):
        if self.items:
            return self.items.pop(0)
        return None

fila = Fila()
fila.adicionar(1)
fila.adicionar(2)
fila.adicionar(3)

print("Retirando da fila:")
while fila.retirar() is not None:
    print(fila.retirar())
