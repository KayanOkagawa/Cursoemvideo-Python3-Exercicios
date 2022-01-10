#-*-coding:utf8;-*-
#qpy:console

titulo = '\033[01;36m'
txt = '\033[36m'
nada = '\033[m'
contador_homem = 0
contador_mulher = 0
contador_maiorm = 0
contador_menorm = 0
contador_maiorf = 0
contador_menorf = 0
contador_vinte = 0

print(f'\n{titulo:-<16} ANÁLISE DE IDADE E SEXO {nada:->11}')

print('\n')

while True:
    sexo = str(input(f'\n{txt}Digite o seu sexo [M/F]:{nada} ')).strip().upper()[0]
    idade = int(input(f'\n{txt}Digite a sua idade:{nada} '))
    if sexo == 'M':
        contador_homem += 1
        if idade >= 18:
            contador_maiorm += 1
        else:
            contador_menorm += 1
    elif sexo == 'F':
        contador_mulher += 1
        if idade >= 18:
            contador_maiorf += 1
        elif idade < 20:
            contador_vinte += 1
        else:
            contador_menotf += 1
    else:
        print('Erro!')
        print('\n')
        print('-' * 42)
    pergunta = str(input(f'\n{txt}Deseja continuar o cadastro:{nada} ')).strip().upper()[0]
    if pergunta == 'S':
        print('\n')
        print('-' * 42)
    elif pergunta == 'N':
        print('\n')
        print('-' * 42)
        print(f'''\n{titulo} RESULTADO {nada}
        	{txt} Maiores de 18: {contador_maiorf + contador_maiorm}
        Quantidade de 	Homens: {contador_homem}
        Mulheres menores de 20: {contador_vinte}{nada}''')
        break
    else:
        print('Erro!')
        print('\n')
        print('-' * 42)
    