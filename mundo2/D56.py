#-*-coding:utf8;-*-
#qpy:console

titulo = '\033[01;32m'
texto = '\033[37m'
nada = '\033[m'
print('\n')
print(titulo, '-' * 10, 'Análise Completa', '-' * 10, nada)
print('\n')
nomes = []
sexos = []
idades = []
maior = 0
media = 0
count = 0
nome = ' '
for c in range(1, 5):
    nome = str(input('Digite o {}° nome: '.format(c)))
    sexo = str(input('Digite o seu sexo da {}° pessoa: '.format(c)))
    idade = int(input('Digite a idade da {}° pessoa: '.format(c)))
    nomes.insert(c-1, nome)
    sexos.insert(c-1, sexo)
    idades.insert(c-1, idade)
    media += idades[c-1]
    sexos.count('masculino')
    if sexos[c - 1] == 'masculino':
        if idades[c - 1] > maior:
            maior = idades[c-1]
            velho = nomes[c-1]
    elif sexos[c-1] == 'feminino':
        if idades[c-1] < 20:
            count += 1
    print('\n')
media = media / 4
print('Média: {}\nMulheres menores de 20: {}\nHomem mais velho: {} '.format(media, count, velho))