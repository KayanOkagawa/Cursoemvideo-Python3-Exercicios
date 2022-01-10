#-*-coding:utf8;-*-
#qpy:console

print('\n')
frase = input('DIGITE UMA FRASE: ').lower().strip()
print('\n')
quantidade = frase.count('a')
p1 = frase.find('a')
p2 = frase.rfind('a')
print(' A quantidade de letras "a" é: {} \n A posição inicial é: {} \n A posição final é: {}'.format(quantidade, p1, p2))