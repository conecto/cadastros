from lib.interface import *

arq = 'cadastrousuarios'
tab = 'pessoas'
titulo('INFORME A FORMA DE ARMAZENAMENTO')
escolha = menu(['Banco de Dados', 'Arquivos txt'])
# Escolha de como gravar os dados adicionados
if escolha == 1:
    from lib.bancoDados import *
    create_bd(arq)
    create_table(arq, tab)
    print('BANCO DE DADOS SELECIONADO!')
else:
    from lib.arquivo import *
    if not arquivoExiste(arq):
        criarArquivo(arq)
    print('ARQUIVOS EM .txt SELECIONADO!')
# Programa Principal
titulo('MENU PRINCIPAL')
while True:
    resposta = menu(['Cadastrar Usuário', 'Consultar Pessoa Cadastrada', 'Sair'])
    if resposta == 1:
        while True:
            subtitulo('Cadastrar usuário')
            nome = input('Nome: ')
            user = usuarioConfirma('Usuário: ', arq, tab)
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
        if escolha == 1:
            cadastrar(arq, tab, nome, user, senha)
        else:
            cadastrar(arq, nome, user, senha)
    elif resposta == 2:
        while True:
            #print(linha())
            subtitulo('Consultar por:')
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
