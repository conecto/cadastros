
from lib.arquivo import *

connection = sqlite3.connect('cad.db')
c = connection.cursor()

create_table()

arq = 'DadosUsuarios.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)
titulo('MENU PRINCIPAL')
while True:
    resposta = menu(['Cadastrar Usuário', 'Consultar Pessoa Cadastrada', 'Sair'])
    if resposta == 1:
        while True:
            subtitulo('Cadastrar usuário')
            nome = input('Nome: ')
            user = usuarioConfirma('Usuário: ', arq)
            senha = leiaSenha('Senha: ')
            while True:
                print(linha())
                conf = input(f"""Confirme seus dados [S/N]:
Nome = {nome}
Usuário = {user}
R: """).strip().upper()[0]
                if conf not in "SN":
                    print('\033[31mDigite uma opção válida!\033[m')
                else:
                    break
            if conf == 'S':
                break

        cadastrar(arq, nome, user, senha)
        dataentry(nome, user, senha)
    elif resposta == 2:
        while True:
            print(linha())
            r = menu(['Nome', 'Usuário', 'Sair'])
            if r == 1:
                lerNome(arq)
            elif r == 2:
                lerUsuario(arq)
            else:
                titulo('Menu Principal')
                break

    elif resposta == 3:
        titulo('Sair, Encerrando O Programa...')
        break
