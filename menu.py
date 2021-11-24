from cores import Cores


def menu():
        
        print(35 * '=')
        print("*** INFORME SEU TIPO DE USUÁRIO ***")
        print(35 * '=')
        print(f"\n{Cores.BOLD}1. Aluno{Cores.ENDC}")
        print(f"{Cores.BOLD}2. Professor{Cores.ENDC}")
        print(f"{Cores.BOLD}{Cores.FAIL}3. Sair{Cores.ENDC}")
        opcaoMenu = int(input("\nSelecione uma opção: "))

        return opcaoMenu


def menuEstudante():

    print(23 * '=')
    print(f"{Cores.BOLD}{Cores.OKBLUE}*** OPÇÃO ESTUDANTE ***{Cores.ENDC}")
    print(23 * '=')
    print(f"{Cores.BOLD}{Cores.FAIL}\n0. Retornar ao menu principal{Cores.ENDC}")
    print(f"{Cores.BOLD}1. Consultar Boletim")
    opcaoMenu = int(input('\nSelecione uma opção: '))

    return opcaoMenu


def menuProfessor():

    print(23 * '=')
    print(f"{Cores.BOLD}{Cores.OKBLUE}*** OPÇÃO PROFESSOR ***{Cores.ENDC}")
    print(23 * '=')
    print(f"{Cores.BOLD}{Cores.FAIL}\n0. Retornar ao menu principal{Cores.ENDC}")
    print(f"{Cores.BOLD}1. Exibir dados")
    print(f"{Cores.BOLD}2. Inserir dados")
    print(f"{Cores.BOLD}3. Atualizar dados")
    print(f"{Cores.BOLD}4. Excluir dados")
    print(f"{Cores.BOLD}5. Pesquisar dados{Cores.ENDC}")

    opcaoMenu = int(input('\nSelecione uma opção: '))
    return opcaoMenu


def submenuCrud():
    
        print(f"{Cores.BOLD}{Cores.OKBLUE}\n*** Selecione um item para modificar os dados ***{Cores.ENDC}")
        print(f"{Cores.BOLD}{Cores.FAIL}\n0. Retornar ao menu principal{Cores.ENDC}")
        print(f"{Cores.BOLD}1. Tipo Usuário")
        print(f"{Cores.BOLD}2. Usuário")
        print(f"{Cores.BOLD}3. Tipo Avaliação")
        print(f"{Cores.BOLD}4. Avaliação")
        print(f"{Cores.BOLD}5. Avaliação Aluno")

        opcaoMenu = int(input('\nSelecione uma opção: '))
        return opcaoMenu


def submenuPesquisar():

    print(f"{Cores.BOLD}{Cores.OKBLUE}\n*** Selecione um item de pesquisa ***{Cores.ENDC}")
    print(f"{Cores.BOLD}{Cores.FAIL}\n0. Retornar ao menu anterior{Cores.ENDC}")
    print(f"{Cores.BOLD}1. Avaliações por período")
    print(f"{Cores.BOLD}2. Avaliações por professor")
    print(f"{Cores.BOLD}3. Avaliações por tipo")
    print(f"{Cores.BOLD}4. Alunos sem avaliações atribuídas")
    print(f"{Cores.BOLD}5. Alunos por situação{Cores.ENDC}")

    opcaoMenu = int(input('\nSelecione uma opção: '))
    return opcaoMenu