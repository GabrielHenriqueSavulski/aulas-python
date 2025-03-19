print('{:=^21}'.format('DESAFIO 064'))

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

c = 0
s = 0
n = 0

while n != 999:
    n = int(input('Digite um número inteiro ou 999 para parar: '))
    s += n
    c += 1

print('Foram digitados {1}{2}{0} números e a soma foi {1}{3}{0}'.format(limpa, azul, c - 1, s - 999))
