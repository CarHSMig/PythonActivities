
def numero_selecionado():
    numero = int(input('Adicione um número para verificarmos se é par ou ímpar: \n'))
    print(f'O número {numero} é {"par" if numero % 2 == 0 else "ímpar"}')

while True:
    numero_selecionado()
    repeticao = int(input('Digite 1 para repetir ou 2 para finalizar: \n'))
    if repeticao == 2:
        break
    