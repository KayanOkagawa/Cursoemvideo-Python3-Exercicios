titulo = '\033[01;33m'
txt = '\033[33m'
nada = '\033[m'
somapar = 0
somacoluna = 0
matriz = [[], [], [], [], [], [], [], [], []]

print(f'\n{titulo:-<17} Criando uma Matriz 2.0 {nada:->12}')

for count in range(0,9):
    num = int(input(f'\n{txt}Digite um número: {nada}'))
    matriz[count].append(num)
    if num % 2 == 0:
        somapar += num
    if count == 2 or count == 8 or count == 5:
        somacoluna += num
print(f'\n{titulo}')
print('-=' * 20)
print('\n')

for count in range(0,9):
    print(f'{matriz[count]}', end=' ')
    if count == 2 or count == 5:
        print('\n')
   

print('\n')
print('-=' * 20)

print(f'A Soma dos valores PAR: {somapar}')
print(f'A Soma da coluna 3: {somacoluna}')
print(f'O Maior valor da linha 2: {max(matriz[3:6])}{nada}')