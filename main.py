import time

from sheet import Sheet
from menu import *
from sqlite import *


if __name__ == '__main__':
    createDb('avaliacao.db')
    connect()
    table()

    opcao = menu()

    while opcao != 3:
        if opcao == 1:
            clean()
            returnMenuEstudante = menuEstudante()
            while returnMenuEstudante != 0:
                if returnMenuEstudante == 1:
                    clean(); boletim()
                    input(f"{Cores.BOLD}{Cores.OKBLUE}\nPressione <ENTER> para voltar ao menu principal ...")
                    print(f'Voltando ao menu principal em 3s...{Cores.ENDC}')
                    time.sleep(3)
                    break
            clean()
            opcao = menu()
        #Menu professor
        elif opcao == 2:
            clean()
            opcaosub = menuProfessor()
            clean()
            while opcaosub != 0:
                if opcaosub == 1:
                    function = 'display'
                elif opcaosub == 2:
                    function = 'insert'
                elif opcaosub == 3:
                    print(f'update')
                    function = 'Update'
                elif opcaosub == 4:
                    print(f'Excluir')
                    function = 'Delete'
                elif opcaosub == 5:
                    print(f'Pesquisar')
                    function = 'query'
                    returnMenuPesquisar = submenuPesquisar()

                    while returnMenuPesquisar != 0:
                        if returnMenuPesquisar == 1:
                            pesquisa = 'AvaliacaoPeriodo'
                        elif returnMenuPesquisar == 2:
                            pesquisa = 'AvaliacaoProfessor'
                        elif returnMenuPesquisar == 3:
                            pesquisa = 'AvaliacaoTipo'
                        elif returnMenuPesquisar == 4:
                            pesquisa = 'AlunosSemAvaliacao'
                        elif returnMenuPesquisar == 5:
                            pesquisa = 'AlunosReprovados'
                        elif returnMenuPesquisar == 6:
                            pesquisa = 'AlunosAprovados'
                        elif returnMenuPesquisar == 7:
                            pesquisa = 'PesquisarNotas'
                        elif returnMenuPesquisar == 8:
                            print('Pesquisar por item')
                            search()
                            input(f"{Cores.BOLD}{Cores.OKBLUE}\nPressione <ENTER> para voltar ao menu principal ...")
                            print(f'Voltando ao menu principal em 3s...{Cores.ENDC}')
                            time.sleep(3)
                            break
                        functions[function + pesquisa]()
                        input(f"{Cores.BOLD}{Cores.OKBLUE}\nPressione <ENTER> para voltar ao menu principal ...")
                        print(f'Voltando ao menu principal em 3s...{Cores.ENDC}')
                        time.sleep(3)
                        clean()
                        break
                    clean()
                    break
                else:
                    print('Opção inválida!')

                returnMenuCrud = submenuCrud()
                while returnMenuCrud != 0:                     
                    if returnMenuCrud   == 1:
                        #table tipoUsuario
                        tabela = 'TipoUsuario'
                    elif returnMenuCrud == 2:
                        #table usuario
                        tabela = 'Usuario'
                    elif returnMenuCrud == 3:
                        #table tipoAvaliacao
                        tabela = 'TipoAvaliacao'
                    elif returnMenuCrud == 4:
                        #table avaliacao
                        tabela = 'Avaliacao'
                    elif returnMenuCrud == 5:
                        #table avaliacaoAluno
                        tabela = 'AvaliacaoAluno'
                    else:
                        print('Opção inválida')

                    if function != 'Update' and function != 'Delete':
                        functions[function + tabela]()
                    elif function == 'Update':
                        update(tabela)
                    elif function == 'Delete':
                        delete(tabela)

                    input(f"{Cores.BOLD}{Cores.OKBLUE}\n\nPressione <ENTER> para voltar ao menu principal ...")
                    print(f'Voltando ao menu principal em 3s...{Cores.ENDC}')
                    time.sleep(3)
                    break
                clean()
                opcaosub = menuProfessor()
                clean()
            opcao = menu()
            clean()
else:
    print("Volte sempre!")
