print('\n\033[01;31mFUNÇÃO DE CONTADOR\033[m')
print('-=' * 30)


def contador(i, f, p=0):
    from time import sleep
    if p < 0:
        p *= -1
    if i > f:
        print(f'\n\033[01;31mCONTADOR DE {i} ATÉ {f} DE {p} EM {p}\033[m')
        p *= -1
        for c in range(i, f-1, p):
            if c == f:
                print(c)
                sleep(1)
            else:
                print(c, end=' ')
                sleep(1)
    else:
        print(f'\n\033[01;31mCONTADOR DE {i} ATÉ {f} DE {p} EM {p}\033[m')
        for c in range(i, f+1, p):
            if c == f:
                print(c)
                sleep(1)
            else:
                print(c, end=' ')
                sleep(1)


contador(1, 10, 1)

contador(10, 0, 2)

inicio = int(input('\nDigite um numero para o inicio: '))
final = int(input('Digite um numero para o fim: '))
passo = int(input('Digite um numero para o passo: '))

contador(inicio, final, passo)
