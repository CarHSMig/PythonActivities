soma_impares = 0

for numero in range(1, 11):  # range vai de 1 a 10
    if numero % 2 != 0:  # verifica se o número é ímpar
        soma_impares += numero

print("A soma dos números ímpares de 1 a 10 é:", soma_impares)