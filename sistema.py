
from lib.arquivo import *

arq = 'DadosUsuarios.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)
titulo('MENU PRINCIPAL')
while True:
    resposta = menu(['Cadastrar Usuário', 'Consultar Pessoa Cadastrada', 'Sair'])
    if resposta == 1:
        subtitulo('Cadastrar usuário')
        nome = input('Nome: ')
        user = usuarioConfirma('Usuário: ', arq)
        senha = leiaSenha('Senha: ')
        cadastrar(arq, nome, user, senha)
    elif resposta == 2:
        while True:
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
