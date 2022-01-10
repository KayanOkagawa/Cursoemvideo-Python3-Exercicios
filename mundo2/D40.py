#-*-coding:utf8;-*-
#qpy:console

from math import ceil
print('\033[31m', '-' * 5, 'MÉDIA DOS ALUNOS', '-' * 5,'\033[m')
print('\n')
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = ceil((n1 + n2) / 2)
print('\n')
if media < 5:
    print('\033[31m', 'Reprovado!', '\033[m')
elif media >= 5 and media <= 6.9:
    print('\033[33m', 'Recuperação!', '\033[m')
elif media >= 7:
    print('\033[32m', 'Aprovado!', '\033[m')
