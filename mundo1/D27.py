#-*-coding:utf8;-*-
#qpy:console

print('\n')
nome = input('DIGITE O SEU NOME: ').title().strip()
print('\n')
lista = nome.split()
print('NOME COMPLETO: {} \n PRIMEIRO NOME: {} \n ÚLTIMO NOME: {}'.format(nome, lista[0], lista[len(lista)-1]))