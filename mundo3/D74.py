from random import randint
tupla = (randint(0,10), randint(0,10),
	randint(0,10), randint(0,10), randint(0,10))
titulo = '\033[01;37m'
txt = '\033[37m'
nada = '\033[m'

print('\n')

print(f'{titulo:-<18} GERADOR DE NÚMEROS {nada:-<15}')

print(f'\nOs valores sorteados foram: ', end='')
for c in tupla:
    print(f'{c}', end='')
print(f'\nMaior: {max(tupla)} \nMenor: {min(tupla)}')

