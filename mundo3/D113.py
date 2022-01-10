def leia_int(msg):
    while True:
        try:
            numero = int(input(f'{msg} '))
        except ValueError:
            print('\033[01;31mErro! Digite um valor inteiro.\033[m')
        except KeyboardInterrupt:
            print('\n\033[01;31mO Usuario desligou o programa.\033[m')
            numero = 0
            return numero
        else:
            return numero


def leia_float(msg):
    while True:
        try:
            numero = float(input(f'{msg} '))
        except ValueError:
            print('\033[01;31mErro! Digite um valor real.\033[m')
        except KeyboardInterrupt:
            print('\n\033[01;31mO Usuario desligou o programa.\033[m')
            numero = 0
            return numero
        else:
            return numero


print('\n\033[01;32mFUNÇÃO LEIA INT E FLOAT\033[m')
print('-=' * 30)

resp_int = leia_int('Digite um número inteiro: ')
resp_float = leia_float('Digite um número real: ')
print(f'\033[07;33mO Valor inteiro foi {resp_int} e o real foi {resp_float}.\033[m')
