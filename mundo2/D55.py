#-*-coding:utf8;-*-
#qpy:console

titulo = '\033[01;36m'
texto = '\033[33m'
nada = '\033[m'
print('\n')
print(titulo, '-' * 10, 'Sequência de Peso', '-' * 10, nada)
print('\n')
maior = 0
menor = 0
for c in range (1, 6):
    peso = float(input('{}Digite o {}° peso:{} '.format(texto, c, nada)))
    if c == 1:
        maior = peso
        menor = peso
    elif peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso
print('\n')
print('{}O Maior peso é {} e o menor é {}.{}'.format(texto, maior, menor, nada))