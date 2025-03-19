print('{:=^21}'.format('DESAFIO 061'))

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

print('{}---CALCULADORA DE P.A.---{}'.format(vermelho, limpa))

n = 1
a1 = int(input('Qual o primeiro termo da P.A.? '))
razao = int(input('Qual a razão da P.A.? '))

print('Os termos da P.A. do a1 até o a10 são:')
while n <= 10:
    an = a1 + (n - 1) * razao
    print(an, end=' ')
    n += 1
