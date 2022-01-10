def interface(conect):
    from time import sleep
    while True:
        print('-=' * 20)
        print('MENU PRINCIPAL')
        print('-=' * 20)

        print("""
1 - Lista Usuarios;
2 - Cadastra Usuarios;
3 - Sair
        """)

        print('-=' * 20)
        opcao = verificador('Sua Opção')
        sleep(1)
        print('-=' * 20)

        if opcao == 1:
            listar(conect)
        elif opcao == 2:
            cadastrar(conect)
        elif opcao == 3:
            print('Desligando o programa...')
            break
        else:
            print('Erro! Digite um opção valida.')


def verificador(msg):
    while True:
        try:
            resp = int(input(f'{msg}: '))
        except ValueError:
            print('\033[01;31mErro! Digite uma opção valida.\033[m')
        except KeyboardInterrupt:
            print('\033[01;31mErro! Usuario desligou o programa.\033[m')
            break
        else:
            return resp


def load_arquivo():
    try:
        arquivo = open('utilidade115/dados.txt', 'r+')
    except FileNotFoundError:
        arquivo = open('utilidade115/dados.txt', 'w')
        return arquivo
    else:
        return arquivo


def listar(conect):
    for n, p in enumerate(conect.readlines()):
        print(f'{n+1}°PESSSOA')
        print(f'NOME: {p[:p.find(";")]}')
        print(f'IDADE: {p[p.find(";")+1:]}')


def cadastrar(conect):
    inf_v = False
    name = str(input('Nome: ')).strip().lower()
    age = str(input('Idade: ')).strip().lower()
    inf = name + ';' + age
    for p in conect.readlines():
        if p == inf:
            inf_v = True
            break
    if inf_v:
        print('\033[01;31mUsuario já existe no sistema.\033[m')
    else:
        conect.write(f'\n{inf}')
        print('\033[01;32mUsuario registrado no sistema.\033[m')

