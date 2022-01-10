nada = '\033[m'
titulo = '\033[01;35m'
txt = '\033[35m'
tupla = (int(input(f'{titulo}\nDigite um número: ')),
	int(input(f'\nDigite um número: ')),
	int(input(f'\nDigite um número: ')),
	int(input(f'\nDigite um número: ')))

print(f'\n{titulo :-<20} ANÁLISE DE TUPLA {nada :->15}')


print(f'\n{txt}Tupla: ', end='')
for count in range(0,4):
    print(f'{tupla[count]}', end='')
print(f'\nQuantidade de 9: {tupla.count(9)}')
if 3 in tupla:
    print(f'\nPosição do 1ª número (3): {tupla.index(3) + 1}')
else:
    print(f'\nPosição do 1ª número (3): 0')
print(f'\nNúmeros Pares: ', end='')
for count in range(0,4):
    if tupla[count] % 2 == 0:
        print(f'{tupla[count]} ', end='')
print(nada)
