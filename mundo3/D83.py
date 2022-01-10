titulo = '\033[01;32m'
txt = '\033[32m'
nada = '\033[m'
lista = list()

print(f'\n{titulo:-<11} Validação de Expressões Matemática {nada:->6}')

expressão = str(input(f'\n{txt}Digite uma expressão: {nada}'))
for c in expressão:
    lista.append(c)
if (lista.count(')') + lista.count('(')) % 2 == 0:
    print(f'\n{titulo}Expressão Aceita{nada}')
else:
    print(f'\n{titulo}Expressão Não Aceita{nada}')