limpa = '\033[m'
negrito = '\033[1m'
sublinhado = '\033[4m'
inversor = '\033[7m'
preto = '\033[30m' # 40 para cor do fundo
vermelho = '\033[31m'
verde = '\033[32m'
amarelo ='\033[33m'
azul = '\033[34m'
roxo = '\033[35m'
ciano = '\033[36m'
cinza = '\033[37m'

from datetime import date

ano = int(input('Qual seu ano de nascimento? '))
data = date.today().year
idade = data - ano
classe = 'a'
if idade <= 9:
    classe = '{}MIRIM{}'.format(vermelho, limpa)
elif 9 < idade <= 14:
    classe = '{}INFANTIL{}'.format(verde, limpa)
elif 14 < idade <= 19:
    classe = '{}JUNIOR{}'.format(amarelo, limpa)
elif 19 < idade <= 25:
    classe = '{}SÊNIOR{}'.format(azul, limpa)
elif 25 < idade:
    classe = '{}MASTER{}'.format(roxo, limpa)
print('Você é da classe de natação {}, segundo a Confederação Nacional de Natação.'.format(classe))