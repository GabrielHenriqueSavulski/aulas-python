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

from datetime import  date

ano = int(input('Qual seu ano de nascimento? '))
data = date.today().year
idade = data - ano

if idade == 18:
    print('Você deve se alistar {1}{2}{3}IMEDIATAMENTE{0},\n'
          'pois tem 18 anos e o alistamento é {1}{2}{3}OBRIGATÓRIO{0}.'
          .format(limpa, vermelho, sublinhado, negrito))
elif idade < 18:
    dif = 18 - idade
    print('Você ainda {1}NÃO{0} tem que se alistar,\n'
          'faltam {1}{2}{3} ANOS{0} para se alistar.'
          .format(limpa, azul, sublinhado, dif))
elif idade > 18:
    dif = idade - 18
    print('Você {1}PASSOU{0} da idade para o alistamento obrigatório,\n'
          'Você {1}DEVIA{0} ter se alistado há {1}{2}{3} ANOS{0}.'
          .format(limpa, amarelo, sublinhado, dif))

