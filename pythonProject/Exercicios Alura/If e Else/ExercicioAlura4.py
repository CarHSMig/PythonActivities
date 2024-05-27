def Verificação_de_quadrantes():
    x = int(input('Digite a coordenada x: \n'))
    y = int(input('Digite a coordenada y: \n'))
    
    if x > 0 and y > 0:
        print('As coordenadas são do primeiro quadrante')
    elif  x < 0 and y > 0:
        print('As coordenadas são do segundo quadrante')
    elif  x < 0 and y < 0:
        print('As coordenadas são do terceiro quadrante')
    elif  x > 0 and y < 0:
        print('As coordenadas são do quarto quadrante')
    else:
        print('As coordenadas são do eixo de origem')

while True:
    Verificação_de_quadrantes()
    repeticao = int(input('Digite 1 para repetir a verificação de idade ou 2 para finalizar: \n'))
    if repeticao == 2:
        break