import os

def exibir_nome_do_programa():
    print("Sabor Express\n")

def exibir_opcoes():
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurante')
    print('3. Ativar Restaurante')
    print('4. Sair\n')

def escolher_opcao():
    opcao_escolhida = int(input('Escolha um opção: '))


    if opcao_escolhida == 1:
        print('Cadastrar restaurante')

    elif opcao_escolhida == 2:
        print('Listar restaurante')

    elif opcao_escolhida == 3:
        print('Ativar restaurante')

    else:
        encerrar_app()


def encerrar_app():
    os.system('cls')
    print('Encerrando o app\n')


def main ():
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()