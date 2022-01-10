#-*-coding:utf8;-*-
#qpy:console

print('\n')
nome = str(input('DIGITE O NOME DA SUA CIDADE: ')).lower().strip()
lista = nome.split()
print('\n')
print('Sua cidade começa com "SANTO": {}'.format('santo' in lista[0]))