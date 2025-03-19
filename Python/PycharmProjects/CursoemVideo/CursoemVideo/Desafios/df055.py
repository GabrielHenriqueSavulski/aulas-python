print('{:=^21}'.format('DESAFIO 055'))

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

p = 10000000000000000000000000000000000000000000000000000
g = 0
for c in range(0, 5):
    peso = float(input('Qual seu peso em Kg? (SOMENTE NÚMEROS) '))
    if peso < p:
        p = peso
    if peso > g:
        g = peso
print('O mais pesado pesa {2}{4}Kg{0} e o mais leve pesa {1}{3}Kg{0}'.format(limpa, verde, vermelho, p, g))
