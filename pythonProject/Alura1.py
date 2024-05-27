import os

restaurantes = [{'nome':'Pizzaria Padilha', 'categoria':'Italiana', 'ativo':True},
                {'nome':'Doceria Amor doce', 'categoria':'Confeitaria', 'ativo': False},
                {'nome':'Takata', 'categoria':'Japonesa', 'ativo':False},]
                

def menu_do_app():
    print('𝓢𝓪𝓫𝓸𝓻 𝓔𝔁𝓹𝓻𝓮𝓼𝓼 \n')

    print('1.Cadastrar restaurante')
    print('2.Listar restaurante')
    print('3.Ativar restaurante')
    print('4.Sair')

def opcao_invalida():
    print('Opção Invalida\n')
    Retornar_menu()
 
def Retornar_menu():
    input('Aperte qualquer tecla para retornar ao menu principal: \n')
    main()
 
def Exibicao_de_programa(texto):
    os.system('cls')
    print(texto)
    
def finalizar_app():
    Exibicao_de_programa('Programa encerrado')

def Cadastrar_restaurantes():
    Exibicao_de_programa('Cadastro de novos restaurantes\n')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}:')
    dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    Retornar_menu()

def listar_restaurantes():
    Exibicao_de_programa('Listagem de restaurantes\n')
    
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria_restaurante = restaurante['categoria']
        presente_no_sistema = 'Restaurante ativo no sistema' if restaurante['ativo'] == True else 'Restaurante não está presente no sistema'
        
        print(f'.{nome_restaurante} - {categoria_restaurante} - ({presente_no_sistema})')
        
    Retornar_menu()
    
def ativar_restaurante():
    Exibicao_de_programa('Implantação de restaurantes no sistema')
    nome_restaurante = input('Digite o nome do restaurante que deseja ativar no sistema: ')
    restaurante_encontrado = False
    
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado == True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso.' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso.'
            print (mensagem)
            
        if not restaurante_encontrado:
            print ('O restaurante não foi encontrado' )
    
    Retornar_menu()
    
def definir_opcao():   
    try:
        opcao_escolhida = int(input('Defina uma opção: \n'))
        print(f'Você escolheu a opção {opcao_escolhida}')

        if opcao_escolhida == 1:
            Cadastrar_restaurantes()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            print('Ativar restaurantes')
        elif opcao_escolhida == 4:
            finalizar_app()
    except:
        opcao_invalida()

def main():
    os.system('cls')
    menu_do_app()
    definir_opcao()

if __name__ == '__main__':
    main()















