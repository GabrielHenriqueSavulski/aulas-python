print('{:=^21}'.format('DESAFIO 041'))

from datetime import  date

limpa = '\033[m'
vermelho = '\033[4;31m'
verde = '\033[4;32m'
amarelo = '\033[4;33m'
azul = '\033[4;34m'
roxo = '\033[4;35m'

data = date.today().year
ano = int(input('Em qual ano você nasceu? '))

idade = int(data - ano)
classe = 'Mirim'

if idade <= 9:
    classe = '{}MIRIM{}'.format(vermelho, limpa)
elif 9 < idade <= 14:
    classe = '{}INFANTIL{}'.format(verde, limpa)
elif 14 < idade <= 19:
    classe = '{}JUNIOR{}'.format(amarelo, limpa)
elif 19 < idade <= 20:
    classe = '{}SÊNIOR{}'.format(azul, limpa)
else:
    classe = '{}MASTER{}'.format(roxo, limpa)
print('A sua categoria de natação, segundo Confederação Nacional de Natação, é {}.'
      .format(classe))
