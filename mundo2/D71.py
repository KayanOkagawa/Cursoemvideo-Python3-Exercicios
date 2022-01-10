titulo = '\033[01;33m'
txt = '\033[33m'
nada = '\033[m'
resto = 1

print(f'\n{titulo:-<23} CAIXA CEV {nada:->18}')

valor = int(input(f'\n{txt}Qual valor você gostaria de sacar:{nada} '))

while True:
    if valor % 50 == 0:
        ced_cinquenta = valor // 50
        print(f'\nNotas R$50: {ced_cinquenta}')
        break
    else:
        ced_cinquenta = valor // 50
        resto = valor % 50
        print(f'\nNotas R$50: {ced_cinquenta}')
        if resto % 20 == 0:
            ced_vinte = resto // 20
            print(f'Notas R$20: {ced_vinte}')
            break
        else:
            ced_vinte = resto // 20
            resto = resto % 20
            print(f'Notad R$20: {ced_vinte}')
            if resto % 10 == 0:
                ced_dez = resto // 10
                print(f'Notas R$10: {ced_dez}')
                break
            else:
                ced_dez = resto // 10
                resto = resto % 10
                print(f'Notas R$10: {ced_dez}')
                if resto % 1 == 0:
                    ced_um = resto // 1
                    print(f'Notas R$1: {ced_um}')
                    break
        