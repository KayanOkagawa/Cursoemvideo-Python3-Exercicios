print('\n\033[01;32mCALCULANDO ÁREA\033[m')
print('-=' * 30)


def area(l, a):
    valor = a * l
    print(f'\033[01;32mA Área do terreno é {valor:.1f}m²\033[m')


largura = float(input('Digite o valor da Largura (m²): '))
altura = float(input('Digite o valor da Altura (m²): '))
area(largura, altura)