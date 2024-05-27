class Pilha:
    def __init__(self):
        self.items = []

    def adicionar(self, item):
        self.items.append(item)

    def retirar(self):
        if self.items:
            return self.items.pop()
        return None

# Exemplo de uso
pilha = Pilha()
pilha.adicionar(1)
pilha.adicionar(2)
pilha.adicionar(3)

print("Retirando da pilha:")
while pilha.retirar() is not None:
    print(pilha.retirar())
