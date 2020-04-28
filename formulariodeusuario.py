
# Criei esse código, vê se é válido ai blz
# Ainda não sei fazer upload de avatar

arquivo = open('arquivo','r+')
pessoa = {}
lista = []
print('='*40)
print(f"{'FORMULÁRIO DE USUÁRIO':^40}")
print('='*40)
while True:
    while True:
        pessoa['nome'] = input('Informe seu nome completo: ').strip()
        while True:
            arquivo = open('arquivo', 'r+')
            u = 0
            pessoa['usuário'] = input('Nome de usuário: ')
            for linha in arquivo:
                if pessoa['usuário'] in linha:
                    print('\033[31mUsuário já existente!\033[m')
                    u = 1
                    break
                else:
                    u = 0
            if u == 0:
                break
        pessoa['senha'] = input('Digite uma senha: ')
        while True:
            csenha = input('Confirme sua senha: ')
            if csenha == pessoa['senha']:
                break
            else:
                print('\033[31mConfirmação inválida.\033[m')
        while True:
            resp = input(f'''Confirme seus dados:
Nome:    {pessoa["nome"]:>20}
Usuário: {pessoa["usuário"]:>20}
{"SIM":>4}{"NÂO":>16}: ''').strip().lower()[0]
            if resp == 's' or resp == 'n':
                break
            else:
                print('\033[31mResposta Inválida.\033[m')
        if resp in 's':
            lista.append(pessoa.copy())
            arquivo.write(f"\n{pessoa['nome']}")
            arquivo.write(f"\n{pessoa['usuário']}")
            arquivo.write(f"\n{pessoa['senha']}")
            pessoa.clear()
            break
        else:
            print('-'*40)
            print(('Insira seus dados novamente: '))
            print('-'*40)
    while True:
        r = input("""O que deseja fazer?
(1) => Adicionar usuário.
(2) => Consultar usuário.
(3) => Sair.""")
        if r not in '123':
            print('\033[31mERRO! Digite um número do menu.\033[m')
        elif r == '1':
            print('\033[33m*** ADICIONANDO NOVO USUÁRIO ***\033[m')
            break
        elif r == '2':
            print('\033[33m***  CONSULTANDO UM USUÁRIO ***\033[m')
            while True:
                escolha = input("""Escolha uma Opção:
(1) => Nome.
(2) => Usuário.""")
                print('='*40)
                if escolha not in '12':
                    print('\033[31mERRO! Digite um número do menu.\033[m')
                else:
                    break
            if escolha == '1':
                while True:
                    c = 0
                    nome = input('Digite o nome, ou (0) para sair: ')
                    if nome == '0':
                        break
                    for p in lista:
                        if p['nome'] == nome:
                            c = 1
                            for k, v in p.items():
                                print(f'{k} é {v}')
                            print()
                    if c == 0:
                        print(f'\033[31mO nome {nome} não foi encontrado.\033[m')
                        print('=' * 40)
            elif escolha == '2':
                c = 0
                while True:
                    user = input('Digite o usuário, ou (0) para sair: ')
                    if user == '0':
                        break
                    for p in lista:
                        if p['usuário'] == user:
                            c = 1
                            for k, v in p.items():
                                print(f'{k} é {v}')
                            print()
                    if c == 0:
                        print(f'\033[31mO usuário {user} não foi encontrado.\033[m')
                        print('=' * 40)
        elif r == '3':
            break
    if r == '3':
        break
arquivo.close()
print(')'*15,'FINALIZANDO', '('*15)