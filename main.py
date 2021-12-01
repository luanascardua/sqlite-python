from sqlite import *
from menu import *
from sheet import *

#print(f'Funções: {functions}')
'''funcao = 'getData'
functions[funcao]()'''

'''function = 'insertUsuario'
functions[function]()'''




'''while True:
    returnMenu = menu()
    clean()
    
    if returnMenu == 3:
        os._exit(1)

    ################ MENU ESTUDANTE ################
    elif returnMenu == 1:
        while True:
            try:
                returnMenuEstudante = menuEstudante()
                if returnMenuEstudante == 1:
                    print('consultar Boletim')
                elif returnMenuEstudante == 0:
                    print('retornar menu principal')
                else:
                    raise ValueError('Opção inválida')
                break
            except ValueError as e:
                print(e)


    ################ MENU PROFESSOR ################
    elif returnMenu == 2:
        returnfunctionessor = menuProfessor()
       
        while returnfunctionessor != 0:
            if returnfunctionessor == 1:
                function = 'display'
            elif returnfunctionessor == 2:
                function = 'insert'
            elif returnfunctionessor == 3:
                function = 'update'
                tabela = input('Tabela: ')
                update(tabela)
                continue
            elif returnfunctionessor == 4:
                function = 'delete'
            elif returnfunctionessor == 5:
                function = 'search'
            else:
                raise ValueError('Opção inválida')
            returnfunctionessor = menuProfessor()
            #except ValueError as e:
                #print(e)
        returnMenu = menu()
        while True:
            try:
                returnMenuCrud = submenuCrud()

                if returnMenuCrud   == 1:
                    #table tipoUsuario
                    functions[function + 'TipoUsuario']()

                elif returnMenuCrud == 2:
                    #table usuario
                    
                    functions[function + 'Usuario']()

                elif returnMenuCrud == 3:
                    #table tipoAvaliacao
                    functions[function + 'TipoAvaliacao']()

                elif returnMenuCrud == 4:
                    #table avaliacao
                    functions[function + 'Avaliacao']()

                elif returnMenuCrud == 5:
                    #table avaliacaoAluno
                    functions[function + 'AvaliacaoAluno']()
                else:
                    raise ValueError('Opção inválida')
                break
            except ValueError as e:
                print(e)
        
    else:
        print('opção Inválida')
    break
'''


if __name__ == '__main__':

    opcao = menu()

    while opcao != 3:
    
        if opcao == 1:
            print('ESTUDANTE')
        elif opcao == 2:
            print('PROFESSOR')
            opcaosub = menuProfessor()
            clean()
            while opcaosub != 0:
                if opcaosub == 1:
                    print(f'Exibir')
                    function = 'display'
                elif opcaosub == 2:
                    print(f'Inserir')
                    function = 'insert'
                elif opcaosub == 3:
                    print(f'update')
                    function = 'Atualizar'
                elif opcaosub == 4:
                    print(f'Excluir')
                    function = 'delete'
                elif opcaosub == 5:
                    print(f'Pesquisar')
                    function = 'search'
                else:
                    print('Opção inválida!')
                opcaosub = menuProfessor()
                clean()
            opcao = menu()
            clean()
else:
    print("Volte sempre!")
