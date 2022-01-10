#-*-coding:utf8;-*-
#qpy:console

titulo = '\033[01;35m'
txt = '\033[38m'
nada = '\033[m'
n = 0
count = 1

print('\n',titulo, '-' * 9, 'GERADOR DE TABUADA', '-' * 9, nada)

while True:
    n = int(input(f'\n{txt} Digite um número:{nada} '))
    print('\n')
    if n >= 0:
        while count <= 10:
            print(f' {n} x {count} = {n * count}')
            count += 1
    else:
        break
    print('\n', titulo, '-' * 38, nada)
    count -= 10
print('\n Fim')