#-*-coding:utf8;-*-
#qpy:console

titulo = '\033[01;37m'
txt = '\033[37m'
nada = '\033[m'
count = 0
n = 0
soma = 0

print('\n')

print(titulo, '-' * 10, 'SOMA DE TUDO', '-' * 10, nada)

print('\n')

print('~ VALOR 999 DESLIGA O PROGRAMA! ~')

print('\n')

while n != 999:
    n = int(input('{}Digite um número:{} '.format(txt, nada)))
    if n != 999:
        count += 1
        soma += n

print('\n')

print('{}~ A soma dos números foi {} e a quantidade de números foi {} ~{}'.format(titulo, soma, count, nada))
        
         
