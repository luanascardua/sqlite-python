from tqdm import tqdm
from sheet import *
import sqlite3
import os


executeWb = Sheet()

clean = lambda: os.system('cls'); clean()


def createDb(database):

    global connection 

    try:
        connection = sqlite3.connect(database)
    except Exception as e:
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
                dataInicio DATE NOT NULL,
                dataTermino DATE NOT NULL,
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
                situacao TEXT NOT NULL,
                FOREIGN KEY (idUser) REFERENCES usuario (idUser),
                FOREIGN KEY (idAvaliacao) REFERENCES avaliacao (idAvaliacao)
                );
        """);

    except Exception as e:
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
    except Exception as e:
        print(e)

    commit()


def insertUsuario():

    executeWb.countLines(sheets[0])
  
    for lines in tqdm(range(executeWb.firstLine, executeWb.lastLine)):
        executeWb.getDataUser(lines)
        print(executeWb.name, executeWb.sigla, executeWb.idade)
        try:
            cursor.execute(
                f"INSERT INTO usuario VALUES(null, '{executeWb.name}', '{executeWb.sigla}', '{executeWb.idade}')"
            )
            print(executeWb.name, executeWb.sigla, executeWb.idade)
        except Exception as e:
            print(e)
        
        commit()


def insertTipoAvaliacao():

    executeWb.countLines(sheets[1])

    for lines in range(executeWb.firstLine, executeWb.lastLine):
        executeWb.getDataTipoAvaliacao(lines)
        try:
            cursor.execute(
                f"INSERT INTO tipoAvaliacao VALUES('{executeWb.sigla}', '{executeWb.descricao}')"
            )
            print(executeWb.sigla, executeWb.descricao)
        except Exception as e:
            print(e)
       
        commit()


def insertAvaliacao():

    executeWb.countLines(sheets[2])

    for lines in tqdm (range(executeWb.firstLine, executeWb.lastLine)):
        executeWb.getDataAvaliacao(lines)
        try:
            cursor.execute(
                f"INSERT INTO tipoAvaliacao VALUES ('{executeWb.sigla}', '{executeWb.descricao}', \
                '{executeWb.dataInicio}', '{executeWb.dataTermino}', '{executeWb.idUser}')"
            )
        except Exception as e:
            print(e)
        print(executeWb.sigla, executeWb.descricao, executeWb.dataInicio, executeWb.dataTermino, executeWb.idUser)
        
        commit()


def insertAvaliacaoAluno():

    executeWb.countLines(sheets[3])

    for lines in tqdm(range(executeWb.firstLine, executeWb.lastLine)):
        executeWb.getDataAvaliacao()
        try:
            cursor.execute(
                f"INSERT INTO avaliacaoAlunos VALUES('{executeWb.idUser}', '{executeWb.idAvaliacao}', \
                '{executeWb.dataConclusao}', '{executeWb.nota}')"
            )
        except Exception as e:
            print(e)


def update(tabela):


    campo  = input('Campo: ')
    update = input('Alterar para: ')
    id     = input('Indique o id a atualizar: ')
    values = (update, id)
    try:
        cursor.execute(
            f"UPDATE '{tabela}' SET '{campo}' =? WHERE idUser = ?;", values
        )
        commit()
        print('Atualizado')
    except Exception as e:
        print(e)


def delete(tabela):

    campo = input('Campo: ')
    value = input('Value: ')
    values = (value,)
    try:
        cursor.execute(
            f"DELETE FROM {tabela} WHERE '{campo}'=?;",values
        )
        commit()
        print('Deletado')
    except Exception as e:
        print(e)



global functions
functions = locals()

createDb('avaliacao.db')
connect()
insertUsuario()
delete('usuario')
