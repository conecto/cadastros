from lib.interface import *


def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('\033[31mHouve ERRO na criação do arquivo\033[m')
    else:
        print(f'\033[32mArquivo {nome} criado com sucesso!\033[m')


def lerNome(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('ERRO ao ler arquivo')
    else:
        while True:
            print(linha())
            print('Digite \033[31mEXIT\033[m para sair.')
            a = open(nome, 'rt')
            s = 0
            n = input('Nome cadastrado: ')
            if n == 'EXIT':
                break
            for l in a:
                dado = l.split(';')
                dado[2] = dado[2].replace('\n', '')
                if dado[0] == n:
                    print(f'Nome: {dado[0]:<31} Usuário: {dado[1]:>3}')
                    s = 1
            if s == 1:
                a.close()
                print(linha())
                break
            else:
                print('\033[31mNome não encontrado\033[m')


def lerUsuario(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except:
        print('ERRO ao ler arquivo')
    else:
        while True:
            print(linha())
            print('Digite \033[31mEXIT\033[m para sair.')
            a = open(nome, 'rt')
            s = 0
            n = input('Usuário cadastrado: ')
            if n == 'EXIT':
                break
            for l in a:
                dado = l.split(';')
                dado[2] = dado[2].replace('\n', '')
                if dado[1] == n:
                    print(f'\033[34mNome:\033[m {dado[0]:<31} \033[34mUsuário:\033[m {dado[1]:>3}')
                    s = 1
            if s == 1:
                a.close()
                print(linha())
                break
            else:
                print('\033[31mUsuário não encontrado\033[m')


def cadastrar(arq, nome='desconhecido', user='desconhecido', senha='***'):
    try:
        a = open(arq, 'at')
    except:
        print('\033[31mHouve um erro na abertura do arquivo!\033[m')
    else:
        try:
            a.write(f'{nome};{user};{senha}\n')
        except:
            print('\033[31mHouve um erro na escrita do arquivo.\033[m')
        else:
            print(f'Novo registro de {nome} adicionado.')
            a.close()
            print(linha())


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


def usuarioConfirma(msg, nome):
    while True:
        s = 0
        u = input(msg)
        a = open(nome, 'rt')
        for l in a:
            dado = l.split(';')
            if dado[1] == u:
                s = 1
        if s == 1:
            print('\033[31mUsuário já cadastrado!\033[m')
        else:
            break
    return u
