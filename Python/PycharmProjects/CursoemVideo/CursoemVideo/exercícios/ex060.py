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

n = int(input('Insira um número para ver o fatorial: '))
m = 1
print('{}! ='.format(n), end=' ')
while n != 0:
    if n == 1:
        print(n, end=' = ')
    else:
        print(n, end=' x ')
    m *= n
    n -= 1
print(m)

#ou

from math import factorial
n = int(input('Insira um número para ver o fatorial: '))
f = factorial(n)
print('O fatorial de {} é {}'.format(n, f))
