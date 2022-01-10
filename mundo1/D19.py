#-*-coding:utf8;-*-
#qpy:console

from random import choice
print('\n')
print('-' * 5, 'SORTEIO DOS ALUNOS', '-' * 5)
print('\n')
n1 = input('Digite o nome do aluno: ')
n2 = input('Digite o nome do aluno: ')
n3 = input('Digite o nome do aluno: ')
n4 = input('Digite o nome do aluno: ')
s = choice([n1, n2, n3, n4])
print('O nome escolhido foi {}'.format(s))
