#-*-coding:utf8;-*-
#qpy:console

print('\n')
nome = str(input('Digite seu nome completo: ')).strip()
print('\n')
u = nome.upper()
l = nome.lower()
lista = nome.split()
letras  = len(nome.replace(' ',''))
p = len(lista[0])
print(' Nome Completo: {} \n Nome Maiúsculo: {} \n Nome Minúsculo: {} \n Nome Sem Espaço: {} letras \n Primeiro Nome: {} letras \n '.format(nome, u, l, letras, p))