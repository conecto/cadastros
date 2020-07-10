import pymysql
from lib.interface import *

conexao = pymysql.connect(
    host='localhost',
    user='root',
    passwd=''
)
cursor = conexao.cursor()


def create_bd(nome):
    try:
        cursor.execute(f"CREATE DATABASE {nome}")
    except:
        print('')


def create_table(bd='', nome=''):
    conexao = pymysql.connect(
        host='localhost',
        user='root',
        passwd='',
        database=bd
    )
    cursor = conexao.cursor()
    try:
        cursor.execute(f"CREATE TABLE {nome} (id INT AUTO_INCREMENT PRIMARY KEY,"
                       " nome VARCHAR (30), usuário VARCHAR(20), senha CHAR(6))")
    except:
        print()


def cadastrar(arq='',tab='desconhecido', nome='desconhecido', user='desconhecido', senha='******'):
    conexao = pymysql.connect(
        host='localhost',
        user='root',
        passwd='',
        database=arq
    )
    cursor = conexao.cursor()
    cursor.execute(f"INSERT INTO {tab} (nome, usuário, senha) VALUES('{nome}', '{user}', '{senha}')")
    conexao.commit()


def usuarioConfirma(msg, arq='', tab=''):
    while True:
        conexao = pymysql.connect(
            host='localhost',
            user='root',
            passwd='',
            database=arq
        )
        cursor = conexao.cursor()
        s = 0
        u = input(msg)
        cursor.execute(f"SELECT * FROM {tab}")
        resultado = cursor.fetchall()
        for l in resultado:
            if l[2] == u:
                s = 1
                break
        if s == 1:
            print('\033[31mUsuário já cadastrado!\033[m')
        else:
            break
    return u


def leiaSenha(msg):
    while True:
        senha = input(msg)
        csenha = input('Confirme sua senha: ')
        if senha == csenha:
            break
        else:
            print('\033[31mERRO! Confirmação Inválida. Tente novamente: \033[m')
            print(linha())
    return senha


def lerNome(arq):
    while True:
        print('Digite \033[31mEXIT\033[m para sair.')
        n = input('\033[34mNome cadastrado\033[m: ')
        if n == 'EXIT':
            break
        conexao = pymysql.connect(
             host='localhost',
             user='root',
             passwd='',
             database=arq,
         )
        cursor = conexao.cursor()
        cursor.execute(f"SELECT * FROM pessoas WHERE nome= '{n}' ")
        resultado = cursor.fetchall()
        for x in resultado:
            print(f' Id      =  {x[0]:>30}\n Nome    =  {x[1]:>30}\n Usuário =  {x[2]:>30}')
        if resultado == ():
            print('\033[31mUsuario nao encontrado\033[m')
        else:
            break


def lerUsuario(arq):
    while True:
        print('Digite \033[31mEXIT\033[m para sair.')
        n = input('\033[34mUsuário cadastrado\033[m: ')
        if n == 'EXIT':
            break
        conexao = pymysql.connect(
             host='localhost',
             user='root',
             passwd='',
             database=arq,
         )
        cursor = conexao.cursor()
        cursor.execute(f"SELECT * FROM pessoas WHERE usuário= '{n}' ")
        resultado = cursor.fetchall()
        for x in resultado:
            print(f' Id      =  {x[0]:>30}\n Nome    =  {x[1]:>30}\n Usuário =  {x[2]:>30}')
        if resultado == ():
            print('\033[31mUsuario nao encontrado\033[m')
        else:
            break