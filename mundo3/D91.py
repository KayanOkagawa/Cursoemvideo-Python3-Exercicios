from random import randint
from time import sleep

titulo = '\033[01;33m'
txt = '\033[33m'
nada = '\033[m'
dados = dict()

print(f'\n{titulo}Valores Sorteados{nada}')
print('\n')

for c in range(0,4):
    valor = dados['jogador-' + str(c+1)] = randint(1,6)
    sleep(1)
    print(f'O Jogador-{c+1} tirou {valor}')

print(f'\n{titulo}Ranking dos Valores{nada}')
print('\n')

c = 1

for v in sorted(dados.values(), reverse=True):
    print(f'Jogador-{c}: {v}')
    c += 1