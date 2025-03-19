print('{:=^21}'.format('DESAFIO 039'))

limpa = '\033[m'
amarelo = '\033[1;4;33m'
vermelho = '\033[1;4;31m'
azul = '\033[4;34m'
verde = '\033[1;4;32m'

idade = int(input('{}Qual a sua idade?{} '.format(azul, limpa)))

if idade < 18:
    print('{}Você ainda vai se alistar, pois tem menos de 18 anos.{}'.format(amarelo, limpa))
elif idade > 18:
    print('{}Você PERDEU o prazo para se alistar, pois já tem mais que 18 anos.{}'.format(vermelho, limpa))
else:
    print('{}VOCÊ DEVE SE ALISTAR, pois já tem 18 anos.{}'.format(verde, limpa))