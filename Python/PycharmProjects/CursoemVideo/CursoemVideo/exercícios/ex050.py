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

for c in range(0, 6):
    número = int(input('Digite um número inteiro: '))
    if número % 2 == 0:
        s += número
        n += 1

print('A soma dos {2}{4}{0} {1}números pares{0} é {2}{3}{0}'.format(limpa, sublinhado, verde, s, n))

