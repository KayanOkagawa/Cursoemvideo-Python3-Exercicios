#-*-coding:utf8;-*-
#qpy:console

titulo = '\033[01;34m'
txt = '\033[33m'
nada = '\033[m'
n = s = count = 0

print('\n', titulo, '-' * 10, 'SOMA DE TODOS', '-' * 10, nada)

print(f'\n{titulo:^12} - 999 FAZ O PROGRAMA PARAR - {nada}')
while True:
    print('\n')
    n = int(input(f'{txt}Digite um número:{nada} '))
    if n == 999:
        break
    s += n
    count += 1
print(f'\n{titulo:^5}~A soma dos números foi {s} e a quantidade de números digitados foi {count}~')