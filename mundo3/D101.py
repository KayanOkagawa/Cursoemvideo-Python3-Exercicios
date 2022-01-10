print('\n\033[01;34mANÁLISE DE VOTO\033[m')
print('-=' * 30)


def voto(ano_nasc):
    from datetime import date
    ano_atual = date.today().year
    idade = ano_atual - ano_nasc
    if 16 < idade < 18 or idade > 70:
        return 'VOTO FACULTATIVO'
    elif 18 <= idade <= 70:
        return 'VOTO OBRIGATORIO'
    else:
        return 'VOTO NEGADO'


ano = int(input('DIGITE O ANO DE NASCIMENTO: '))
print(f'\033[07;34m{voto(ano)}\033[m')
