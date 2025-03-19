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

s = 0
n = 0

for c in range(3, 500, 3):
    if c % 2 != 0:
        s += c
        n += 1

print('A soma dos {1}{2}{0} números solicitados deu {1}{3}{0}'.format(limpa, vermelho, n, s))
