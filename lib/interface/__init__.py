def linha(tam=52):
    return "-" * tam


def titulo(msg):
    print(linha())
    print(f'\033[33m{msg.center(len(linha()))}\033[m')
    print(linha())


def subtitulo(msg):
    print(linha())
    print(f'\033[33m{msg}\033[m')
    print(linha())


def menu(lista):
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m ')
        c += 1
    print(linha())
    while True:
        opc = leiaint('\033[32mSua Opção:\033[m ')
        if opc < 1 or opc >= c:
            print('\033[31mERRO! Digite uma opção válida.\033[m')
        else:
            break
    return opc


def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: Por favor digite um número inteiro válido!\033[m')
            continue
        else:
            return n
