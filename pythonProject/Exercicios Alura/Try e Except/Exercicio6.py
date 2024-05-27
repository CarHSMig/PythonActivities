
numeros = [1, 2, 3, 4, 5]

soma = 0
for numero in numeros:
    try:
        soma += numero
    except TypeError as e:
        print("Erro:", e)

print("A soma dos elementos da lista é:", soma)