titulo = '\033[01;32m'
txt = '\033[32m'
nada = '\033[m'
matriz = [[], [], [],
[], [], [],
[], [], []]

print(f'\n{titulo:-<16} Criando uma Matriz 1.0 {nada:->13}')

for count in range(0,9):
    num = int(input(f'\n{txt}Digite um número: {nada}'))
    matriz[count].append(num)
print('\n','-=' * 20)
print('\n')
for count in range(0,9):
    print(f'{titulo}{matriz[count]}', end=' ')
    if count == 2 or count == 5:
        print('\n')
print('\n')