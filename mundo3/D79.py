titulo = '\033[01;36m'
txt = '\033[36m'
nada = '\033[m'
erro = '\033[01;31m'
sucesso = '\033[01;32m'
resposta = 'S'
lista = list()

print(f'\n{titulo:-<16} Análise de Valor Único {nada:->13}')

while True:
    if resposta in 'S':
        lista.append(int(input(f'\n{txt}Digite um número: {nada}')))
        if len(lista) > 1:
            if lista.count(lista[len(lista)-1]) > 1:
                for c in range(0, len(lista)-1):
                    if lista[len(lista)-1] == lista[c]:              
                        lista.pop()
                        print(f'\n{erro}Valor repetido, não foi possível adicionar!{nada}')
                        break
            else:
                print(f'\n{sucesso}Valor Adicionado com Sucesso!{nada}')
        else:
            print(f'\n{sucesso}Valor Adicionado com Sucesso!{nada}')
    
    resposta = ' '
    
    while not resposta in 'SN':
        resposta = input(f'\n{txt}Deseja continuar? [S/N]: {nada}').strip().upper()[0]
    
    print(f'\n{titulo:-<33}{nada:->20}')
    
    if resposta in 'N':
        lista.sort()
        print(f'\n{titulo}O valores salvos foram: ', end=' ')
        for c in lista:
            print(c, end=' ')
        break