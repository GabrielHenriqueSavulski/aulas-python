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

n = int(input('Digite qual número você quer a tabuada: '))

for c in range(0, 11):
    r = c * n
    print('{1}{3}{0} X {2}{4}{0} = {5}{6}{0}'.format(limpa, vermelho, azul, n, c, amarelo, r))
