def leiaint(msg):
    while True:
        num = str(input(f'{msg} ')).strip()
        if num.isnumeric():
            return num
        else:
            print('\033[01;31mERRO! Digite um número inteiro válido.\033[m')


resp = leiaint('Digite um Número:')
print(f'\033[07;32mO Número Digitado foi: {resp}\033[m')
