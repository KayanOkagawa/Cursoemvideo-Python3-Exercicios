#-*-coding:utf8;-*-
#qpy:console

from random import shuffle
print('\n')
print('-' * 5, 'SORTEIO DA APRESENTAÇÃO', '-' * 5)
print('\n')
n1 = input('Digite o nome do aluno(a): ')
n2 = input('Digite o nome do aluno(a): ')
n3 = input('Digite o nome do aluno(a): ')
n4 = input('Digite o nome do alumo(a): ')
nomes = [n1, n2, n3, n4]
shuffle(nomes)
print('\n')
print('A ordem de apresentação é {}, {}, {} e {}'.format(nomes[0], nomes[1], nomes[2], nomes[3]))
