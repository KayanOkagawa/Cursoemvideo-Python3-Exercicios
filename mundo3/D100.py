print('\n\033[01;31mFUNÇÃO SORTEIO LISTA E SOMAPAR\033[m')
print('-=' * 30)

lista = list()


def sorteio(l):
    from random import randint
    for c in range(0, 5):
        l.append(randint(0, 10))
    print(l)


def somapar(l):
    soma = 0
    for c in l:
        if c % 2 == 0:
            soma += c
    print(soma)


sorteio(lista)
somapar(lista)