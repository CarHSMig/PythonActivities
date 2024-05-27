numero = int(input('Digite o número que deseja multiplicar: \n'))
print(f'Aqui está a tabuada do número digitado: \n')

for i in range(1, 11):
    if i < 11:
        print(f'{i} x {numero}: {i*numero}')