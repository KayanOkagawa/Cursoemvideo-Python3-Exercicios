#-*-coding:utf8;-*-
#qpy:console

import random, time

titulo = '\033[01;37m'
texto = '\033[34m'
nada = '\033[m'
count = 0
jogador = ' '
com = 0

print('\n')

print(titulo, '-' * 10, 'Jogo de Adivinhação', '-' * 10, nada)

print('\n')

pergunta = str(input('{} Quer jogar ? [Sim/Não]: {}'.format(texto, nada))).upper()[0].strip()
if pergunta == 'S':
    time.sleep(1)
    while jogador != com:
        jogador = int(input('\n{} Adivinhe o número que estou pensando: {}'.format(texto, nada)))
        com = random.randint(1,10)
        count += 1
        if jogador != com:
            print('\n JOGADOR: {} \n COM: {}'.format(jogador, com))
            print(' Você Errou! Tente novamente.')
        else:
            print('\n', '-' * 40)
            print('\n Você Ganhou!')
            print('\n Tentativas: {}'.format(count))
else:
    print('\n', '-' * 40)
    print('\n Ok, Tchau')