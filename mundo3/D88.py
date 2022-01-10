from time import sleep
from random import randint

titulo = '\033[01;36m'
txt = '\033[36m'
nada = '\033[m'
jogos = list()
sorteio = list()

print(f'\n{titulo:-<17} Gerador de Mega Sena {nada:->14}')

quantidade = int(input(f'\n{txt}Digite a quantidade de jogos: {nada}'))

for teste in range(0, quantidade):
    for count in range(0, 6):
        num = randint(0,60)
        if count == 0:
            sorteio.append(num)
        while num in sorteio:
            num = randint(0,60)
        sorteio.append(num)
    sorteio.sort()
    jogos.append(sorteio[:])
    sorteio.clear()

print(f'\n{titulo}Jogos Sorteados')
for c in jogos:
    sleep(1)
    print(f'\n{c}')
