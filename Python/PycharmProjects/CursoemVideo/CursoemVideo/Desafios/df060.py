print('{:=^21}'.format('DESAFIO 060'))

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

a = int(input('Quer o fatorial de qual número? '))
c = a
multi = 1
while c > 0:
    multi *= c
    c = c - 1

print('{}! = {}'.format(a, multi))
