print('{:=^21}'.format('DESAFIO 063'))

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

print('-' * 30)
print('Sequencia de Fibonacci')
print('-' * 30)
termos = int(input('Quantos termos  você quer ver? '))
t1 = 0
t2 = 1
n = 3

print('~' * 30)
print('{} --> {} -->'.format(t1, t2), end=' ')
while n <= termos:
    t = t1 + t2
    print(t, end=' --> ')
    n += 1
    t1 = t2
    t2 = t
