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

n = int(input('Digite um número: '))
d = 0

for c in range(1, n + 1):
    if n % c == 0:
        print(azul, end='')
        d += 1
    else:
        print(vermelho, end='')
    print('{}{} '.format(c, limpa), end='')
if d == 2:
    print('\nO número {1}{2} é primo{0}, pois tem {1}{3}{0} divisores'.format(limpa, azul, n, d))
else:
    print('\nO número {1}{2} não é primo{0}, pois tem {1}{3}{0} divisores'.format(limpa, vermelho, n, d))
