#-*-coding:utf8;-*-
#qpy:console

ciano = '\033[36m'
vermelho = '\033[31m'
amarelo = '\033[33m'
nada = '\033[m'
print(vermelho, '-' * 5, nada, ciano, 'CALCULADORA IMC', nada, vermelho, '-' * 5, nada)
print('\n')
altura = float(input('Digite a sua altura: '))
peso = float( input('Digite o seu peso: '))
imc = peso/(altura * altura)
print('\n')
if imc < 18.5:
    print(vermelho, 'Abaixo do Peso!', nada)
elif imc >= 18.5 and imc <= 25:
    print(ciano, 'Peso Ideal!', nada)
elif imc > 25 and imc <= 30:
    print(amarelo, 'Sobrepeso!', nada)
elif imc > 30 and imc <= 40:
    print(vermelho, 'Obesidade!', nada)
elif imc > 40:
    print(vermelho, 'Obesidade Mórbida!', nada)
