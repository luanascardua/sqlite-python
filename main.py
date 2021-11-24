from sqlite import *
from menu import *
from sheet import *

#print(f'Funções: {functions}')
'''funcao = 'getData'
functions[funcao]()'''

'''function = 'insertUsuario'
functions[function]()'''




while True:
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

        while True:
            try:
                returnfunctionessor = menuProfessor()
                
                if returnfunctionessor   == 0:
                    print('voltar')
                elif returnfunctionessor == 1:
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
                break
            except ValueError as e:
                print(e)

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
executeDb.createDb()
executeDb.connect()
executeDb.table()
executeDb.insertTipoUsuario()
executeDb.insertUsuario()'''