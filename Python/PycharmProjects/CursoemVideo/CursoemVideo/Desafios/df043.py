print('{:=^21}'.format('DESAFIO 043'))

limpa = '\033[m'
azul = '\033[34m'
verde = '\033[32m'
amarelo = '\033[33m'
roxo = '\033[35m'
vermelho = '\033[31m'

altura = float(input('Escreva sua altura em metros, por exemplo 1.61: '))
peso = float(input('Escreva se peso em kilos, por exemplo 36.5: '))

imc = peso / (altura ** 2)

resultado = ''
if imc < 18.5:
    resultado = '{}ABAIXO DO PESO{}, procure um médico.'.format(azul, limpa)
elif 18.5 <= imc <= 25:
    resultado = '{}peso normal.{}'.format(verde, limpa)
elif 25 < imc <= 30:
    resultado = '{}sobrepeso.{}'.format(amarelo,limpa)
elif 30 < imc <= 40:
    resultado = '{}OBESIDADE{}, procure um médico.'.format(roxo, limpa)
else:
    resultado = '{}OBESIDADE MÓRBIDA{}, procure um médico.'.format(vermelho, limpa)

print('Seu imc teve um resultado de: {}'.format(resultado))
