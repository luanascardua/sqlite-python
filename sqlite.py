from sqlite3 import Error
from cores import Cores
from tqdm import tqdm
from sheet import *
import sqlite3
import time
import os


executeWb = Sheet()

clean = lambda: os.system('cls'); clean()


def createDb(database):

    global connection 

    try:
        connection = sqlite3.connect(database)
    except sqlite3.Error as e:
        print(e)


def connect():

    global cursor
    cursor = connection.cursor()


def commit():
    
    connection.commit()


def table():


    #criar tabela tipoUsuario
    try:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tipoUsuario(
                siglaUsuario TEXT PRIMARY KEY,
                descricao TEXT NOT NULL
                );
        """)

        #criar tabela usuario
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuario(
                idUser INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                siglaUsuario TEXT NOT NULL,
                idade INTEGER NOT NULL,
                FOREIGN KEY (siglaUsuario) REFERENCES tipoUsuario (siglaUsuario)
                );
        """)

        #criar tabela tipoAvaliacao
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tipoAvaliacao(
                siglaAvalicao TEXT PRIMARY KEY,
                descricao TEXT NOT NULL
                );
        """)

        #criar tabela avaliacao
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS avaliacao(
                idAvaliacao INTEGER PRIMARY KEY,
                siglaAvaliacao TEXT NOT NULL,
                descricao TEXT NOT NULL,
		        tipoAvaliacao TEXT NOT NULL,
                dataInicio DATE ONLY NOT NULL,
                dataTermino DATE ONLY NOT NULL,
		        notaAprovacao FLOAT NOT NULL,
                idUser INTEGER,
                FOREIGN KEY (idUser) REFERENCES usuario (idUser),
                FOREIGN KEY (siglaAvaliacao) REFERENCES tipoAvaliacao (siglaAvaliacao)
                );
        """)

        #criar tabela avaliacaoAluno
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS avaliacaoAluno(
                idUser TEXT NOT NULL,
                idAvaliacao TEXT NOT NULL,
                dataConclusao DATE,
                notaAtribuida REAL NOT NULL,
                FOREIGN KEY (idUser) REFERENCES usuario (idUser),
                FOREIGN KEY (idAvaliacao) REFERENCES avaliacao (idAvaliacao)
                );
        """);

    except sqlite3.Error as e:
        print(e)

    
def insertTipoUsuario():
    
    tipoUsuario = [
        ('PROF', 'Professor'),
        ('ESTD', 'Estudante')
    ]
    

    try:
        cursor.executemany(
            "INSERT INTO tipoUsuario VALUES (?,?);", tipoUsuario
        )
        print(f'{Cores.OKGREEN}\nDados inseridos com sucesso.')
    except Error as e:
        print(e)

    commit()


def insertUsuario():

    executeWb.countLines(sheets[0])
    
    for lines in tqdm(range(executeWb.firstLine, executeWb.lastLine)):
        executeWb.getDataUser(lines)
        try:
            cursor.execute(
                f"INSERT INTO usuario VALUES(null, '{executeWb.name}', '{executeWb.sigla}', '{executeWb.idade}')"
            )

            commit()
        except Exception as e:
            print(e)

        executeWb.insertData(lines)
        
    print(f'{Cores.OKGREEN}\nDados inseridos com sucesso.')
    

def insertTipoAvaliacao():

    executeWb.countLines(sheets[1])

    for lines in tqdm(range(executeWb.firstLine, executeWb.lastLine)):
        executeWb.getDataTipoAvaliacao(lines)
        
        try:
            cursor.execute(
                f"INSERT INTO tipoAvaliacao VALUES('{executeWb.sigla}', '{executeWb.descricao}')"
            )
        except Exception as e:
            print(e)
       
        commit()
        executeWb.insertData(lines)

    print(f'{Cores.OKGREEN}\nDados inseridos com sucesso.')


def insertAvaliacao():

    executeWb.countLines(sheets[2])

    for lines in tqdm(range(executeWb.firstLine, executeWb.lastLine)):
        executeWb.getDataAvaliacao(lines)

        try:
            cursor.execute(
                f"INSERT INTO avaliacao VALUES (null, '{executeWb.sigla}', '{executeWb.descricao}', \
                '{executeWb.tipoAvaliacao}', '{executeWb.dataInicio}', '{executeWb.dataTermino}', \
                '{executeWb.notaAprovacao}', '{executeWb.idUser}')"
            )
        except Exception as e:
            print(e)
        
        commit()
        executeWb.insertData(lines)

    print(f'{Cores.OKGREEN}\nDados inseridos com sucesso.')


def insertAvaliacaoAluno():

    executeWb.countLines(sheets[3])

    for lines in tqdm(range(executeWb.firstLine, executeWb.lastLine)):
        executeWb.getDataAvaliacaoAluno(lines)
        
        try:
            cursor.execute(
                f"INSERT INTO avaliacaoAluno VALUES('{executeWb.idUser}', '{executeWb.idAvaliacao}', \
                '{executeWb.dataConclusao}', '{executeWb.nota}')"
            )
        except Exception as e:
            print(e)

        commit()
        executeWb.insertData(lines)

    print(f'{Cores.OKGREEN}\nDados inseridos com sucesso.')


def update(tabela):
   
    print(f'{Cores.BOLD}{Cores.OKBLUE}\n*** Preencha as informações ***\n{Cores.ENDC}')
    
    campo  = input('CAMPO: ')
    update = input('ALTERAR PARA: ')
    id     = input('INDIQUE O ID A ATUALIZAR: ')
    values = (update, id)

    try:
        cursor.execute(
            f"UPDATE '{tabela}' SET '{campo}' =? WHERE idUser = ?;", values
        )
        commit()
        print(f'{Cores.OKGREEN}\nCampo atualizado com sucesso.{Cores.ENDC}')
    except Exception as e:
        print(e)


def delete(tabela):

    print(f'{Cores.BOLD}{Cores.OKBLUE}\n*** Preencha as informações ***\n{Cores.ENDC}')

    campo = input('CAMPO DE REFERÊNCIA: ')
    value = input('VALUE: ')
    
    try:
        cursor.execute(
            f"DELETE FROM {tabela.lower()} WHERE {campo} = '{value}'"        )
        commit()
        print(f'{Cores.OKGREEN}\nCampo excluído com sucesso.')
    except Exception as e:
        print(e)


#listar elementos das tabelas
def displayTipoUsuario():
    
    try:
        cursor.execute(
            "SELECT * FROM tipoUsuario"
            )
        resultado = cursor.fetchall()

        if resultado:
            print(f'{Cores.BOLD}{Cores.OKGREEN}')
            print('{:<10} {:<20}'.format('Sigla', 'Descrição'))
            print(25 * '_'); print(f'{Cores.ENDC}')
            for item in range(len(resultado)):
                print("{:<10} {:<20}".format(resultado[item][0], resultado[item][1]))
        else:
            print(f'{Cores.BOLD}{Cores.FAIL}Não foram encontrados registros.{Cores.ENDC}')
    except Exception as e:
        print(e)


def displayUsuario():

    try:
        cursor.execute(
            "SELECT * FROM usuario"
            )
        resultado = cursor.fetchall()

        if resultado:
            print(f'{Cores.BOLD}{Cores.OKGREEN}')
            print('{:<10} {:<30} {:<10} {:<5}'.format('ID', 'NOME', 'SIGLA', 'IDADE'))
            print(60 * '_'); print(f'{Cores.ENDC}')

            for item in range(len(resultado)):
                print("{:<10} {:<30} {:<10} {:<5}".format(resultado[item][0], resultado[item][1],
                resultado[item][2], resultado[item][3]))
        else:
            print(f'{Cores.BOLD}{Cores.FAIL}Não foram encontrados registros.{Cores.ENDC}')
    except Exception as e:
        print(e)
    

def displayTipoAvaliacao():

    try:
        cursor.execute(
            "SELECT * FROM tipoAvaliacao"
            )
        resultado = cursor.fetchall()

        if resultado:
            print(f"{Cores.BOLD}{Cores.OKGREEN}")
            print("{:<10} {:<20}".format("Sigla", "Descrição"))
            print(25 * '_'); print(f"{Cores.ENDC} ")
            for item in range(len(resultado)):
                print("{:<10} {:<20}".format(resultado[item][0], resultado[item][1]))
        else:
            print(f"{Cores.BOLD}{Cores.FAIL}Não foram encontrados registros.{Cores.ENDC}")

    except Exception as e:
        print(e)


def displayAvaliacao():

    try:
        cursor.execute("""
            SELECT idAvaliacao, siglaAvaliacao, descricao, tipoAvaliacao, date(dataInicio), date(dataTermino), notaAprovacao, idUser 
            FROM avaliacao
        """)

        resultado = cursor.fetchall()
    
        if resultado:
            print(f"{Cores.BOLD}{Cores.OKGREEN}")
            print("{:<5} {:<10} {:<30} {:<10} {:<15} {:<15} {:<10} {:<10}".format("ID", "SIGLA", "DESCRIÇÃO", "TIPO", "DATA INÍCIO",
                "DATA TÉRMINO", "NOTA", "ID USER"))
            print(110 * '_'); print(f"{Cores.ENDC} ")

            for item in range(len(resultado)):
                print('{:<5} {:<10} {:<30} {:<10} {:<15} {:<15} {:<10} {:<10}'.format(resultado[item][0], resultado[item][1], 
                resultado[item][2], resultado[item][3], resultado[item][4], resultado[item][5], resultado[item][6], resultado[item][7]))
        else:
            print(f"{Cores.BOLD}{Cores.FAIL}Não foram encontrados registros.{Cores.ENDC}")

    except Exception as e:
        print(e)


def displayAvaliacaoAluno():

    try:
        cursor.execute("""
            SELECT idUser, idAvaliacao, date(dataConclusao), notaAtribuida
            FROM avaliacaoAluno
        """)

        resultado = cursor.fetchall()
    
        if resultado:
            print(f"{Cores.BOLD}{Cores.OKGREEN}")
            print("{:<10} {:<10} {:<15} {:<10}".format("ID User", "ID Aval", "DATA conclusão", "NOTA"))
            print(45 * '_'); print(f"{Cores.ENDC} ")

            for item in range(len(resultado)):
                print('{:<10} {:<10} {:<15} {:<10}'.format(resultado[item][0], resultado[item][1], 
                resultado[item][2], resultado[item][3]))
        else:
            print(f"{Cores.BOLD}{Cores.FAIL}Não foram encontrados registros.{Cores.ENDC}")

    except Exception as e:
        print(e)


def queryAvaliacaoPeriodo():

    #Por periodo
    print(f'{Cores.BOLD}{Cores.OKBLUE}\n*** Preencha as informações ***\n{Cores.ENDC}')
    periodoInicio   = input('Data início: ')
    periodoTermino  = input('Data término: ')

    try:
        cursor.execute(
           f"""SELECT idAvaliacao, siglaAvaliacao, descricao, date(dataInicio), date(dataTermino), notaAprovacao, idUser 
            FROM avaliacao WHERE dataInicio >= '{periodoInicio}' AND dataTermino <= '{periodoTermino}'
        """)

        resultado = cursor.fetchall()
      
        if resultado:
            print(f"{Cores.BOLD}{Cores.OKGREEN}")
            print("{:<10} {:<10} {:<30} {:15} {:<15} {:<10} {:<10}".format("ID", "SIGLA", "DESCRIÇÃO", "DATA Início",
                "DATA Término", "NOTA", "ID User"))
            print(110 * '_'); print(f"{Cores.ENDC} ")
    
            for item in range(len(resultado)):
                print("{:<10} {:<10} {:<30} {:15} {:<15} {:<10} {:<10}".format(resultado[item][0], resultado[item][1], 
                resultado[item][2], resultado[item][3], resultado[item][4], resultado[item][5], resultado[item][6],))
        else:
            print(f"{Cores.BOLD}{Cores.FAIL}Não foram encontrados registros.{Cores.ENDC}")
        
    except Exception as e:
        print(e)


def queryAvaliacaoProfessor():

    #Por professor
    professor = input('\nProfessor: ')
   
    try:
        cursor.execute(
            f"""SELECT A.idAvaliacao, A.siglaAvaliacao, A.descricao, date(A.dataInicio), date(A.dataTermino), U.nome
            FROM avaliacao AS A INNER JOIN usuario AS U ON A.idUser = U.idUser
            WHERE u.nome LIKE '%{professor}%' AND u.siglaUsuario = 'PROF';
        """)

        resultado = cursor.fetchall()

        if resultado:
            print(f"{Cores.BOLD}{Cores.OKGREEN}")
            print("{:<10} {:<10} {:<20} {:<15} {:<15} {:<20}".format("ID", "SIGLA", "DESCRIÇÃO", "DATA Início",
            "DATA Término", "PROFESSOR"))
            print(90 * '_'); print(f"{Cores.ENDC} ")
        
            for item in range(len(resultado)):
                print("{:<10} {:<10} {:<20} {:<15} {:<15} {:<20}".format(resultado[item][0], resultado[item][1], resultado[item][2], resultado[item][3], 
                resultado[item][4], resultado[item][5]))       
        else:
            print(f"{Cores.BOLD}{Cores.FAIL}Não foram encontrados registros.{Cores.ENDC}")
    except Exception as e:
        print(e)
    

def queryAvaliacaoTipo():

    tipo = input('\nTipo: ')

    try:
        cursor.execute(
            f"""SELECT idAvaliacao, siglaAvaliacao, descricao, tipoAvaliacao, date(dataInicio), date(dataTermino), notaAprovacao
            FROM avaliacao WHERE tipoAvaliacao = '{tipo.upper()}'
        """)

        resultado = cursor.fetchall()
      
        if resultado:
            print(f"{Cores.BOLD}{Cores.OKGREEN}")
            print("{:<10} {:<10} {:<20} {:<10} {:<15} {:<15} {:<10}".format("ID", "SIGLA", "DESCRIÇÃO", "TIPO",
            "DATA Início", "DATA Término", "NOTA Aprovação"))
            print(100 * '_'); print(f"{Cores.ENDC} ")
        
            for item in range(len(resultado)):
                print("{:<10} {:<10} {:<20} {:<10} {:<15} {:<15} {:<10}".format(resultado[item][0], resultado[item][1], 
                resultado[item][2], resultado[item][3], resultado[item][4], resultado[item][5], resultado[item][6]))
        else:
            print(f"{Cores.BOLD}{Cores.FAIL}Não foram encontrados registros.{Cores.ENDC}")
    except Exception as e:
        print(e)


def queryAlunosSemAvaliacao():

    #alunos sem nota atribuída
    try:
        cursor.execute("""
            SELECT U.idUser, U.nome, U.siglaUsuario, AA.notaAtribuida 
            FROM usuario as U LEFT JOIN avaliacaoAluno as AA on U.idUser = AA.idUser
            WHERE U.siglaUsuario = 'ESTD' and AA.notaAtribuida is null
            GROUP BY U.idUser;
        """)

        resultado = cursor.fetchall()
       
        if resultado:
            print(f"{Cores.BOLD}{Cores.OKGREEN}")
            print("{:<10} {:<20} {:<10}".format("ID", "NOME", "SIGLA"))
            print(30 * '_'); print(f"{Cores.ENDC} ")
    
            for item in range(len(resultado)):
                print("{:<10} {:<20} {:<10}".format(resultado[item][0], resultado[item][1], resultado[item][2]))
        else:
            print(f"{Cores.BOLD}{Cores.FAIL}Não foram encontrados registros.{Cores.ENDC}")

    except Exception as e:
        print(e)


def queryAlunosReprovados():

    #lista alunos reprovados
    try:
        cursor.execute("""
            SELECT U.nome, A.siglaAvaliacao, AA.notaAtribuida
            FROM usuario as U LEFT JOIN avaliacaoAluno as AA
            ON U.idUser = AA.idUser
            LEFT JOIN avaliacao as A
            ON AA.idAvaliacao = A.idAvaliacao
            WHERE U.siglaUsuario = 'ESTD' and AA.notaAtribuida < A.notaAprovacao;
        """)

        resultado = cursor.fetchall()

        if resultado:
            print(f"{Cores.BOLD}{Cores.OKGREEN}")
            print("{:<20} {:<10} {:<10}".format("ESTUDANTE", "SIGLA", "NOTA"))
            print(40 * '_'); print(f"{Cores.ENDC} ")
    
            for item in range(len(resultado)):
                print("{:<20} {:<10} {:<10}".format(resultado[item][0], resultado[item][1], resultado[item][2]))
        else:
            print(f"{Cores.BOLD}{Cores.FAIL}Não foram encontrados registros.{Cores.ENDC}")

    except Exception as e:
        print(e)


def queryAlunosAprovados():

    #lista alunos aprovados
    try:
        cursor.execute("""
            SELECT U.nome, A.siglaAvaliacao, AA.notaAtribuida
            FROM usuario as U LEFT JOIN avaliacaoAluno as AA
            ON U.idUser = AA.idUser
            LEFT JOIN avaliacao as A
            ON AA.idAvaliacao = A.idAvaliacao
            WHERE U.siglaUsuario = 'ESTD' and AA.notaAtribuida >= A.notaAprovacao;
        """)

        resultado = cursor.fetchall()

        if resultado:
            print(f"{Cores.BOLD}{Cores.OKGREEN}")
            print("{:<20} {:<10} {:<10}".format("ESTUDANTE", "SIGLA", "NOTA"))
            print(40 * '_'); print(f"{Cores.ENDC} ")
    
            for item in range(len(resultado)):
                print("{:<20} {:<10} {:<10}".format(resultado[item][0], resultado[item][1], resultado[item][2]))
        else:
            print(f"{Cores.BOLD}{Cores.FAIL}Não foram encontrados registros.{Cores.ENDC}")

    except Exception as e:
        print(e)


def queryPesquisarNotas():

    #pesquisa e lista avaliações entre notas 
    print(f'{Cores.BOLD}{Cores.OKBLUE}\n*** Preencha as informações ***\n{Cores.ENDC}')
    i = input('Nota inicial: ')
    f = input('Nota final: ')

    try:
        cursor.execute(
            f"""SELECT U.nome, A.siglaAvaliacao, AA.notaAtribuida
            FROM usuario as U LEFT JOIN avaliacaoAluno as AA
            ON U.idUser = AA.idUser
            LEFT JOIN avaliacao as A
            ON AA.idAvaliacao = A.idAvaliacao
            WHERE U.siglaUsuario = 'ESTD' and AA.notaAtribuida >={i} and AA.notaAtribuida <= {f};
        """)

        resultado = cursor.fetchall()

        if resultado:
            print(f"{Cores.BOLD}{Cores.OKGREEN}")
            print("{:<20} {:<10} {:<10}".format("ESTUDANTE", "SIGLA", "NOTA"))
            print(40 * '_'); print(f"{Cores.ENDC} ")
    
            for item in range(len(resultado)):
                print("{:<20} {:<10} {:<10}".format(resultado[item][0], resultado[item][1], resultado[item][2]))
        else:
            print(f"{Cores.BOLD}{Cores.FAIL}Não foram encontrados registros.{Cores.ENDC}")

    except Exception as e:
        print(e)


def search():

    #Ppesquisa algum registro de acordo com o dado do campo informado
    print(f'{Cores.BOLD}{Cores.OKBLUE}\n*** Preencha as informações ***\n{Cores.ENDC}')
    
    tabela   = input('TABELA: ')
    campo    = input('CAMPO: ')
    registro = input('REGISTRO: ')
  
    try:
        cursor.execute(
            f"SELECT * FROM {tabela} WHERE {campo} like '%{registro}%'"
        )
        resultado = cursor.fetchall()
        print('\n')

        if resultado:
            for item in range(len(resultado)):
                print(resultado[item])
        else:
            print(f"{Cores.BOLD}{Cores.FAIL}Não foram encontrados registros.{Cores.ENDC}")

    except Exception as e:
        print(e)


def boletim():

    #lista todas as avaliações e notas correspondentes ao nome do estudante informado 
    estudante = input('\nInforme seu nome: ')

    try:
        cursor.execute(
            f"""SELECT A.siglaAvaliacao, AA.notaAtribuida
            FROM avaliacaoAluno as AA INNER JOIN usuario as U
            ON AA.idUser = U.idUser
            INNER JOIN avaliacao as A
            ON AA.idAvaliacao = A.idAvaliacao
            WHERE U.siglaUsuario = 'ESTD' and U.nome LIKE '%{estudante}%';
        """)
        resultado = cursor.fetchall()

        if resultado:
            print(f"{Cores.BOLD}{Cores.OKGREEN}")
            print("{:<10} {:<10}".format("SIGLA", "NOTA"))
            print(f"{Cores.ENDC} ")

            for item in range(len(resultado)):
                print("{:<10} {:<10}".format(resultado[item][0], resultado[item][1]))
        else:
            print(f"{Cores.BOLD}{Cores.FAIL}Não foram encontrados registros.{Cores.ENDC}")

    except Exception as e:
        print(e)



global functions
functions = locals()

createDb('avaliacao.db')
connect()
table()
