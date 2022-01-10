#-*-coding:utf8;-*-
#qpy:console

titulo = '\033[01;36m'
txt = '\033[36m'
nada = '\033[m'
count = 0
maior = 0
menor = 0
media = 0
soma = 0
resposta = 'S'

print('\n', titulo, '-' * 9, 'MÉDIA DOS VALORES', '-' * 9, nada)

while resposta == 'S':
    print('\n', '~' * 40)
    n = int(input('\n{} Digite um número:{} '.format(txt, nada)))
    count += 1
    soma += n
    if count == 1:
        maior = n
        menor = n
    elif maior < n:
        maior = n
    elif menor > n:
        menor = n
    resposta = str(input('\n{} Gostaria de continuar? [S/N]:{} '.format(txt, nada))).strip().upper()[0]
    print('\n', '~' * 40, '\n')
media = soma / count
print('\nMÉDIA: {:.2f} \nMAIOR: {} \nMENOR: {}'.format(media, maior, menor))
