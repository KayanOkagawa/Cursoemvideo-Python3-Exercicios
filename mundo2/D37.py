#-*-coding:utf8;-*-
#qpy:console

import math
nada = '\033[m'
title = '\033[01;34m'
amarelo = '\033[33m'
rosa = '\033[35m'
caule = ("""
	⣿⣿⣿⣿⠿⢋⣩⣤⣴⣶⣶⣦⣙⣉⣉⣉⣉⣙⡛⢋⣥⣶⣶⣶⣶⣶⣬⡙⢿⣿ 
	⣿⣿⠟⣡⣶⣿⢟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠙ 
	⣿⢋⣼⣿⠟⣱⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⢿⣿⣿⣿⣿⣧ 
	⠃⣾⣯⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣿⣿⡈⢿⣿⣿⣿⣿ 
	⢰⣶⣼⣿⣷⣿⣽⠿⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡌⣿⣷⡀⠛⢿⣿⣿ 
	⢃⣺⣿⣿⣿⢿⠏⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡾⣿⣿⣿⣷⢹⣿⣷⣄⠄⠈⠉ 
	⡼⣻⣿⣷⣿⠏⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣞⣿⣿⣿⠸⣿⣿⣿⣿⣶⣤ 
	⣇⣿⡿⣿⠏⣸⣎⣻⣟⣿⣿⣿⢿⣿⣿⣿⣿⠟⣩⣼⢆⠻⣿⡆⣿⣿⣿⣿⣿⣿ 
	⢸⣿⡿⠋⠈⠉⠄⠉⠻⣽⣿⣿⣯⢿⣿⣿⡻⠋⠉⠄⠈⠑⠊⠃⣿⣿⣿⣿⣿⣿ 
	⣿⣿⠄⠄⣰⠱⠿⠄⠄⢨⣿⣿⣿⣿⣿⣿⡆⢶⠷⠄⠄⢄⠄⠄⣿⣿⣿⣿⣿⣿ 
	⣿⣿⠘⣤⣿⡀⣤⣤⣤⢸⣿⣿⣿⣿⣿⣿⡇⢠⣤⣤⡄⣸⣀⡆⣿⣿⣿⣿⣿⣿ 
	⣿⣿⡀⣿⣿⣷⣌⣉⣡⣾⣿⣿⣿⣿⣿⣿⣿⣌⣛⣋⣴⣿⣿⢣⣿⣿⣿⣿⡟⣿ 
	⢹⣿⢸⣿⣻⣶⣿⢿⣿⣿⣿⢿⣿⣿⣻⣿⣿⣿⡿⣿⣭⡿⠻⢸⣿⣿⣿⣿⡇⢹ 
	⠈⣿⡆⠻⣿⣏⣿⣿⣿⣿⣿⡜⣭⣍⢻⣿⣿⣿⣿⣿⣛⣿⠃⣿⣿⣿⣿⡿⠄⣼ 
	⣦⠘⣿⣄⠊⠛⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⣼⣿⣿⣿⡿⠁⠄⠟
	""")
print('\n')
print(title, '-' * 10, 'CONVERSOR DE BASES', '-' * 10, nada,'\n')
print('{}\n'.format(caule))
print('''\n\033[01;034mBASES PARA CONVERSÃO\033[m\n
\033[33m(1) Binária
(2) Octal
(3) Hexadecimal\033[m
''')
escolha = int(input('\nOPCÃO: '))
n = int(input('\n\033[33mDigite um número: \033[m'))
if escolha == 1:
    print('\n{}{} convertido para Binário é {}{}'.format(rosa,n, bin(n)[2:], nada))
elif escolha == 2:
    print('\n{}{} convertido para Octal é {}{}'.format(rosa, n, oct(n)[2:], nada))
elif escolha == 3:
    print('\n{}{} convertido para Hexadecimal é {}{}'.format(rosa, n, hex(n)[2:], nada))
else:
    print('Opção Inválida!')
