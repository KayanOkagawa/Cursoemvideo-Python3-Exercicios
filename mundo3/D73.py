ranking = ('Atlético-MG', 'Flamengo', 'Fortaleza', 'Palmeiras', 'Bragantino', 'Corinthians', 'Internacional', 'Fluminense', 'Cuiabá', 'Athletico-PR', 'Atlético-GO' , 'América-MG', 'Ceará SC', 'São Paulo', 'Santos', 'Bahia', 'Juventude', 'Sport-Recife', 'Grêmio', 'Chapecoense')
titulo = '\033[01;36m'
txt = '\033[36m'
nada = '\033[m'

print('\n')

print(f'{titulo:-<17} TABELA DO BRASILEIRÃO {nada:->13}')

print('\n')

print(f'''{titulo} -> PRIMEIROS COLOCADOS {nada}
{txt}

 {ranking[:5]}
 
{nada}
 
{titulo} -> ÚLTIMOS COLOCADOS {nada}

{txt}
 
 {ranking[-4:]}
 
{nada}

{titulo} -> TABELA EM ORDEM ALFABÉTICA {nada}

{txt}

 {sorted(ranking)}
 
{nada}

{titulo} -> POSIÇÃO DA CHAPECOENSE {nada}

{txt}

 O time da Chapecoense tá na {ranking.index('Chapecoense')+1}° posição

{nada}
 
''')
 