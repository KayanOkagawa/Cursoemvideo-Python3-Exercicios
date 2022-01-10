def help_system(msg):
    from time import sleep
    while True:
        print('\033[01;32mSISTEMA DE HELP\033[m')
        print('-=' * 30)
        system = str(input(f'{msg} ')).strip().lower()
        print('-=' * 30)
        if system == 'fim':
            print('FINALIZANDO...')
            break
        print(f'\033[01;32mACESSEANDO O MANUAL DO COMANDO "{system}"\033[m')
        sleep(1)
        print('\033[07;32m')
        help(f'{system}')
        print('\033[m')
        print('-=' * 30)


help_system('Digite uma FUNÇÃO ou BIBLIOTECA:')
