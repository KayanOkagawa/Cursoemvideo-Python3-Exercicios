titulo = '\033[01;33m'
txt = '\033[33m'
nada = '\033[m'
dados = dict()

print(f'\n{titulo}Analise de Media{nada}')

dados['nome'] = str(input(f'\n{txt}Digite o seu nome: '))
dados['media'] = float(input(f'\nDigite a media do {dados["nome"]}: '))

if dados['media'] >= 7:
    dados['situacao'] = 'Aprovado'
elif 5 > dados['media'] < 7:
    dados['situacao'] = 'Recuperação'
else:
    dados['situacao'] = 'Reprovado'
print(f'\nNome: {dados["nome"]} \nMedia: {dados["media"]} \nSituacao: {dados["situacao"]}')
