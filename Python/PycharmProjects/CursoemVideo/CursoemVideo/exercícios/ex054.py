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
adulto = 0
menor = 0
for c in range(0, 7):
    ano = int(input('Qual o ano de nascimento: '))
    if data - ano > 18:
        adulto += 1
    else:
        menor += 1

print('Foram inseridos {1}{4} {3}adultos{0} e {2}{5} {3}menores{0}.'
      .format(limpa, vermelho, azul, sublinhado, adulto, menor))
