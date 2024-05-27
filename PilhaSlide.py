class Pilha:
    def __init__(self):
        self.items = []

    def vazia(self):
        return self.items == []

    def empilhar(self, item):
        self.items.append(item)

    def desempilhar(self):
        return self.items.pop()

    def tamanho(self):
        return len(self.items)

    def topo(self):
        return self.items[-1] if not self.vazia() else None

minha_pilha = Pilha()
minha_pilha.empilhar(1)
minha_pilha.empilhar(2)
minha_pilha.empilhar(3)

print("Topo da pilha:", minha_pilha.topo())
print("Tamanho da pilha:", minha_pilha.tamanho())

while not minha_pilha.vazia():
    print("Desempilhando:", minha_pilha.desempilhar())

def inverter_pilha(pilha):
    pilha_invertida = Pilha()
    while not pilha.vazia():
        pilha_invertida.empilhar(pilha.desempilhar())
    return pilha_invertida

minha_pilha = Pilha()
minha_pilha.empilhar(1)
minha_pilha.empilhar(2)
minha_pilha.empilhar(3)

pilha_invertida = inverter_pilha(minha_pilha)

while not pilha_invertida.vazia():
    print("Desempilhando da pilha invertida:", pilha_invertida.desempilhar())