print('\n\033[01;31mFUNÇÃO VERIFICADOR DE MAIOR E MENOR\033[m')
print('-=' * 30)


def func_maior(*num):
    maior = 0
    menor = 0
    from time import sleep
    print(f'\n\033[01;31mANALISANDO OS VALORES...\033[m')
    sleep(1)
    for c in range(0, len(num)):
        if c == 0:
            maior = num[c]
            menor = num[c]
        elif num[c] > maior:
            maior = num[c]
        else:
            menor = num[c]
        print(num[c], end=' ')
        sleep(1)
    print(f'Foram informados {len(num)} valores ao todo.')
    print(f'O Maior valor informado foi {maior} e o Menor {menor}')


func_maior(4, 3, 2, 1, 9, 4)
func_maior(4, 7, 0)
func_maior(1, 2)
func_maior(6)
func_maior()
