#-*-coding:utf8;-*-
#qpy:console

titulo = '\033[01;35m'
texto = '\033[35m'
nada = '\033[m'
escolha = ' '
resposta = ' '

print('\n')

print(titulo, '-' * 15, '1° Menu', '-' * 15, nada)

print('\n')

n1 = int(input('Digite o 1° número: '))
n2 = int(input('Digite o 2° número: '))

print('\n')

while escolha != 5:
    print("""
    	[1] Soma 
    	[2] Multiplicação 
    	[3] Maior 
    	[4] Trocar números 
    	[5] Sair do Programa
    	""")
    escolha = int(input('Escolha uma opção: '))
    
    print('\n')
    
    if escolha == 1:    
        resposta = n1 + n2
        print('SOMA = {}'.format(resposta))
        print(texto,'-' * 42, nada)
    
    elif escolha == 2:
        resposta = n1 * n2
        print('MULTIPLICAÇÃO = {}'.format(resposta))
        print(texto,'-' * 42, nada)
    
    elif escolha == 3:
        if n1 > n2:
            resposta = n1
            print('MAIOR = {}'.format(resposta))
            print(texto, '-' * 42,nada)
        else:
            resposta = n2
            print('MAIOR = {}'.format(resposta))
            print(texto, '-' * 42, nada)
    
    elif escolha == 4:
        n1 = int(input('Digite um novo número: '))
        n2 = int(input('Digite outro número: '))
        print(texto, '-' * 42, nada)
    else:
        print('Erro! Opção Inválida.')
        print(texto, '-' * 42, nada)