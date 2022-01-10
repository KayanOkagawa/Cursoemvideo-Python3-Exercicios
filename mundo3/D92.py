# Importa a função datetime do modulo datetime
from datetime import datetime

# Cria um Dicionario
dados = dict()

print('\n\033[01;31mAVALIANDO DADOS E APOSENTADORIA\033[m')
print('-=' * 30)

# Recebe os Dados no dicionario
dados['nome'] = input('Digite o seu Nome: ')
dados['idade'] = datetime.today().year - int(input('Digite o ano de Nascimento: '))
dados['ctps'] = int(input('Digite o número da CTPS: (Digite 0 se não tiver) '))

if dados['ctps'] != 0:
    dados['contratação'] = str(input('Digite o ano de contratação: '))
    dados['salario'] = int(input('Digite o salário recebido: '))
    dados['aposentadoria'] = 62 - dados['idade']

    print('\n\033[01;31mDADOS CADASTRADOS\033[m')
    print('-=' * 30)

    for k, v in dados.items():
        print(f'{k.upper()}: {v}')

else:
    print('\n\033[01;31mDADOS CADASTRADOS\033[m')
    print('-=' * 30)

    for k, v in dados.items():
        print(f'{k.upper()}: {v}')