#-*-coding:utf8;-*-
#qpy:console

from random import randint
print('\n')
print('-' * 5, 'ADIVINHE O NÚMERO', '-' * 5)
print('\n')
opção = input('Quer jogar comigo: ').lower().strip()
print('\n')
if opção == 'sim':
    print('Muito bom! Adivinhe o número que estou pensando entre 0 a 5')
    print('\n')
    n = randint(0,5)
    resposta = int(input('Digite o número: '))
    if resposta == n:
        print('Parabens! Você acertou!')
    else:
        print('Você errou!')

elif opção == 'não' or opção == 'nao':
    print('Ok!')
else:
    print('Não entendi.')    
print('\n')
print('Fim')

        
