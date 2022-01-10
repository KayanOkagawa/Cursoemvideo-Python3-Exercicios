#-*-coding:utf8;-*-
#qpy:console

titulo = '\033[01;34m'
txt = '\033[34m'
nada = '\033[m'
contador_mil = 0
count = 1
anterior = 0
total = 0

print(f'\n{titulo:-<19} Análise de Produto {nada :->14}')

while True:
    nome = str(input(f'\n{txt}Digite o nome do Produto:{nada} ')).strip()
    preço = float(input(f'\n{txt}Digite o valor do Produto:{nada} '))
    if count == 1:
        produto_barato = nome
        total = preço
        anterior = preço
        if preço > 1000:
            contador_mil += 1
    elif count > 1:
        if preço < anterior:
            anterior = preço
            produto_barato = nome
            total += preço
            if preço > 1000:
                contador_mil += 1
        else:
            total += preço
            if preço > 1000:
                contador_mil += 1
    count += 1
    pergunta = str(input(f'\n{txt}Gostaria de continuar a compra:{nada} ')).strip().upper()[0]
    if pergunta == 'S':
        print('\n')
        print('-' * 42)
    elif pergunta == 'N':
        print('\n')
        print('-' * 42)
        print(f'''{titulo} RESULTADO {nada}

TOTAL: R${total:.2f}
MAIORES QUE 1000: {contador_mil}
PRODUTO MAIS BARATO: {produto_barato}''')
        break
    else:
        print('Erro!')
    
            
