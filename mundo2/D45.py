#-*-coding:utf8;-*-
#qpy:console
 
import random, time
nada = '\033[m'
titulo = '\033[01;33m'
texto = '\033[36m'
print('\n')
print(titulo,'-' * 9, 'VAMOS JOGAR JOKÊMPO!', '-' * 9, nada)
print('\n')
escolha = ['pedra', 'tesoura', 'papel']
teste = str(input('\033[36mDigite a sua escolha: \033[m')).strip().lower()
com = random.choice(escolha)
print('\n')
print(titulo, 'Carregando...', nada)
time.sleep(1.5)
print('\n')
if teste == com:
    print(' VOCÊ: {} \n COMPUTADOR: {}'.format(teste, com))
    print('\n')
    print('Empate!')
elif not teste == com:
    if teste == 'tesoura' and com == 'pedra':
        print(' VOCÊ: {} \n COMPUTADOR: {}'.format(teste, com))
        print('\n')
        print('Você Perdeu!')
    elif teste == 'tesoura' and com == 'papel':
        print(' VOCÊ: {} \n COMPUTADOR: {}'.format(teste, com))
        print('\n')
        print('Você Ganhou!')
    elif teste == 'pedra' and com == 'papel':
        print(' VOCÊ: {} \n COMPUTADOR: {}'.format(teste, com))
        print('\n')
        print('Você Perdeu!')
    elif teste == 'pedra' and com == 'tesoura':
        print(' VOCÊ: {} \n COMPUTADOR: {}'.format(teste, com))
        print('\n')
        print('Você Ganhou!')
    elif teste == 'papel' and com == 'tesoura':
        print(' VOCÊ: {} \n COMPUTADOR: {}'.format(teste, com))
        print('\n')
        print('Você Perdeu!')
    elif teste == 'papel' and com == 'pedra':
        print(' VOCÊ: {} \n COMPUTADOR: {}'.format(teste, com))
        print('\n')
        print('Você Ganhou!')
    