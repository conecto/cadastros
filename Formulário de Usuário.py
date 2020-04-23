
# Criei esse código, vê se é válido ai blz
# Ainda não sei fazer upload de avatar

pessoa = {}
lista = []
print('='*26)
print(f"{'FORMULÁRIO DE USUÁRIO':^26}")
print('='*26)
while True:
    pessoa['nome'] = input('Informe seu nome completo: ').strip().title()
    while True:
        pessoa['user'] = input('Nome de usuário: ')
        if pessoa['user'] != lista[0]['user']:
            break
        else:
            print('\033[33mUsuário não esta disponível\033[m')
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
Usuário: {pessoa["user"]:>20}
{"SIM":>4}{"NÂO":>16}: ''').strip().lower()[0]
        if resp == 's' or resp == 'n':
            break
        else:
            print('\033[31mResposta Inválida.\033[m')
    if resp in 's':
        break
    else:
        print('-'*26)
        print(('Insira seus dados novamente: '))
        print('-'*26)
