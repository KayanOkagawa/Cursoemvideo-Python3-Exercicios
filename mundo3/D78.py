titulo = '\033[01;34m'
txt = '\033[34m'
nada = '\033[m'
lista = list()

print(f'\n{titulo:-<17} Analisando uma Lista {nada:->14}')

for count in range(0,5):
    lista.append(int(input(f'\n{txt}Digite um número: {nada}')))

maior = max(lista)
menor = min(lista)

print(f'\n{txt:-<47}')

if lista.count(maior) > 1:
    print(f'\n{titulo}O Maior valor foi: {maior} nas posições', end=' ')
    for c in range(0, lista.count(maior)):
        if c == 0:
            psmaior = lista.index(maior)
            print(psmaior + 1, end='...')
        else:
            psmaior = lista.index(maior, psmaior + 1)
            print(psmaior + 1, end='...')
else:
    print(f'\n{titulo}O Maior valor foi: {maior} na posição {lista.index(maior) + 1}')

if lista.count(menor) > 1:
    print(f'\n{titulo}O Menor valor foi: {menor} nas posições', end=' ')
    for c in range(0, lista.count(menor)):
        if c == 0:
            psmenor = lista.index(menor)
            print(psmenor + 1, end='...')
        else:
            psmenor = lista.index(menor, psmenor + 1)
            print(psmenor + 1, end='...')
else:
    print(f'\nO Menor valor foi: {menor} na posição {lista.index(menor)+1}{nada}')
