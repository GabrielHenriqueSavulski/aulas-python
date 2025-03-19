print('{:=^21}'.format('DESAFIO 054'))

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

data = date.today().year
m = 0
p = 0
for c in range(0, 7):
    nasc = int(input('Ano de nascimento: '))
    if data - nasc < 21:
        p += 1
    elif data - nasc >= 21:
        m += 1
print('O total de pessoas com menos de 21 anos é {1}{3}{0} e o total, com 21 anos ou mais é {2}{4}{0}'
      .format(limpa, verde, vermelho, p, m))
