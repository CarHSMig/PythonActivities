
class Fila:
    def __init__(self):
        self.items = []

    def vazia(self):
        return self.items == []

    def tamanho(self):
        return len(self.items)

    def enfileirar(self, item):
        self.items.append(item)

    def desenfileirar(self):
        if not self.vazia():
            return self.items.pop(0)
        else:
            return None

    def frente(self):
        if not self.vazia():
            return self.items[0]
        else:
            return None

fila = Fila()
print("A fila está vazia?", fila.vazia())

fila.enfileirar(1)
fila.enfileirar(2)
fila.enfileirar(3)

print("A fila está vazia?", fila.vazia())
print("Tamanho da fila:", fila.tamanho())

print("Primeiro elemento da fila:", fila.frente())

print("Desenfileirando:", fila.desenfileirar()) 
print("Tamanho da fila após desenfileirar:", fila.tamanho()) 