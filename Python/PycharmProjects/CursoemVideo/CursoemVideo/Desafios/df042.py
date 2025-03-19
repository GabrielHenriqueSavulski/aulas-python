print('{:=^21}'.format('DESAFIO 042'))

l1 = float(input('Lado 1: '))
l2 = float(input('Lado 2: '))
l3 = float(input('Lado 3: '))

limpa = '\033[m'
amarelo = '\033[33m'
vermelho = '\033[31m'
verde = '\033[32m'
azul = '\033[34m'
roxo = '\033[35m'

triangulo = False
if l1 + l2 > l3 and l2 + l3 > l1 and l1 + l3 > l2:
    triangulo = True

if triangulo == True:
    print('{}Forma um triângulo do tipo:{}'.format(verde, limpa))
    if l1 == l2 != l3 or l2 == l3 != l1 or l1 == l3 != l2:
        print('{}ISÓCELES{}'.format(roxo, limpa))
    elif l1 == l2 == l3:
        print('{}EQUILÁTERO{}'.format(azul, limpa))
    elif l1 != l2 != l3 != l1:
        print('{}ESCALENO{}'.format(amarelo, limpa))
else:
    print('{}Não forma triângulo.{}'.format(vermelho, limpa))
