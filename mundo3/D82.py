titulo = '\033[01;33m'
txt = '\033[37m'
nada = '\033[m'
lista = list()
par = list()
impar = list()
resposta = 'S'

print(f'\n{titulo:-<20} Lista Par e Impar {nada:->14}')

while True:
    if resposta == 'S':
        lista.append(int(input(f'\n{txt}Digite um número: {nada}')))
        resposta = ' '
    while not resposta in 'SN':
        resposta = input(f'\n{txt}Você deseja continuar ? [S/N]: {nada}').strip().upper()[0]
    if resposta == 'N':
        print(len(lista))
        for count in range(0, len(lista)):
            if lista[count] % 2 == 0:
                par.append(lista[count])
            else:
                impar.append(lista[count])
        print(f'\n{titulo}Lista Original:', end=' ')
        for c in lista:
            print(c, end=' ')
        print('\nLista Par:', end=' ')
        for c in par:
            print(c, end=' ')
        print('\nLista Impar:', end=' ')
        for c in impar:
            print(c, end=' ')
        print(f'{nada}')
        break