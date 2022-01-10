#-*-coding:utf8;-*-
#qpy:console

from random import randint

titulo = '\033[01;32m'
txt = '\033[32m'
nada = '\033[m'
com = ' '
count = 0
jg = ' '

print('\n', titulo, '-' * 10, 'PAR OU IMPAR', '-' * 10, nada)

print(f'\n OS VALORES DEVEM SER ENTRE 0 E 10')

while True:     
    jg = str(input(f'\n {txt}Escolha Impar ou Par:{nada} ')).strip().upper()[0]
    if jg == 'P':
        com = 'I'
        esc_jg = int(input(f'\n {txt}Escolha um número ({jg}):{nada} '))
        esc_com = randint(0,10)
        soma = esc_jg + esc_com
        if soma % 2 == 0:
            print('\n Você Venceu')
            print(f'\n JOGADOR: {esc_jg} \n COM: {esc_com} \n TENTATIVAS: {count}')
            print('\n')
            print('-' * 42)
            count += 1
        else:
            print('\n Você Perdeu')
            print(f'\n JOGADOR: {esc_jg} \n COM: {esc_com} \n TENTATIVAS: {count}')
            print('\n')
            print('-' * 42)
            break
    elif jg == 'I':
        com = 'P'
        esc_jg = int(input(f'\n {txt}Escolha um número ({jg}):{nada} '))
        esc_com = randint(0,10)
        soma = esc_jg + esc_com
        if soma % 2 == 0:
            print('\n Você Perdeu')
            print(f'\n JOGADOR: {esc_jg} \n COM: {esc_com} \n TENTATIVAS: {count}')
            print('\n')
            print('-' * 42)
            break
        else:
            print('\n Você Ganhou')
            print(f'\n JOGADOR: {esc_jg} \n COM: {esc_com} \n TENTATIVAS: {count}')
            print('\n')
            print('-' * 42)
            count += 1