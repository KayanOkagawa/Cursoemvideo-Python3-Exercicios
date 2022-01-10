def leia_dinheiro(msg):
    while True:
        numero = input(f'{msg} ').strip()
        if numero.isnumeric():
            return float(numero)
        elif numero.isalnum() or numero.isalpha():
            print('\033[01;31mERRO! Digite um valor númerico.\033[m')
        else:
            if numero.find(',') >= 0 or numero.find('.') >= 0:
                if numero.find(',') >= 0:
                    numero.replace(',', '.')
                pos = numero.find('.')
                if numero[0:pos].isnumeric() and numero[pos+1:].isnumeric():
                    num_int = int(numero[0:pos])
                    if len(numero[pos+1:]) == 2:
                        num_float = float(numero[pos+1:]) / 100
                    else:
                        num_float = float(numero[pos+1:] + '0') / 100
                    return num_int + num_float
                else:
                    print('\033[01;31mERRO! Digite um valor númerico.\033[m')
