def Confirmacao_de_idade():
    numero = int(input('Digite sua idade por gentileza: \n'))
    if numero < 12:
        print('Você é uma criança')
    elif numero >= 12 and numero < 18:
        print('Você é um adolescente')
    else:
        print('Você é adulto')

while True:
    Confirmacao_de_idade()
    repeticao = int(input('Digite 1 para repetir a verificação de idade ou 2 para finalizar: \n'))
    if repeticao == 2:
        break